import sqlite3 as sql
from pathlib import Path

from nonebot.log import logger
from nonebot import require

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as localstore

from .utils import wrap


class Database:
    def __init__(self):
        self.file = localstore.get_plugin_data_file("drop.db")
        self.database = sql.connect(self.file)
        self.cursor = self.database.cursor()

        try:
            self.cursor.execute(
                """
                create table if not exist drop_log (
                    user_id     text,
                    date        text,
                    knife       text,
                    loss        float,
                    primary key (user_id, date)
                """
            )
            self.database.commit()
        except sql.Error as error:
            logger.error(f"Error occurs when creating table 'drop_log' in 'drop.db': {str(error)}")

    def __del__(self):
        self.cursor.close()
        self.database.close()

    def insert(self, info: dict) -> None:
        self.cursor.execute(
            "insert into drop_log (user_id, date, knife, loss) values (?, ?, ?, ?)",
            (info.get('user_id'), info.get('date'), info.get('knife'), info.get('loss'))
        )
        self.database.commit()

    def remove(self, user_id: str, date: str) -> None:
        self.cursor.execute(
            "delete from drop_log where user_id = ? and date = ?",
            (user_id, date)
        )
        self.database.commit()

    def query(self, user_id: str, date: str) -> None | dict:
        self.cursor.execute(
            "select user_id, date, knife, loss from drop_log where user_id = ? and date = ?",
            (user_id, date)
        )
        result = self.cursor.fetchone()
        return None if result is None else wrap(result)
