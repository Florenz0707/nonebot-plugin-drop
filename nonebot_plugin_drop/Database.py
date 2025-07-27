import sqlite3 as sql

from nonebot.log import logger
from nonebot import require

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as localstore

from .utils import wrap


class Database:
    def __init__(self):
        self._file = localstore.get_plugin_data_file("drop.db")
        self._database = sql.connect(self._file)
        self._cursor = self._database.cursor()

        try:
            self._cursor.execute(
                """
                create table if not exists drop_log
                (
                    user_id text,
                    date    text,
                    knife   text,
                    loss    float,
                    primary key (user_id, date)
                )
                """
            )
            self._database.commit()
        except sql.Error as error:
            logger.error(f"Error occurs when creating table 'drop_log' in 'drop.db': {str(error)}")

    def __del__(self):
        self._cursor.close()
        self._database.close()

    def insert(self, user_id: str, date: str, knife: str, loss: float) -> None:
        self._cursor.execute(
            "insert into drop_log (user_id, date, knife, loss) values (?, ?, ?, ?)",
            (user_id, date, knife, loss)
        )
        self._database.commit()

    def remove(self, user_id: str, date: str) -> None:
        self._cursor.execute(
            "delete from drop_log where user_id = ? and date = ?",
            (user_id, date)
        )
        self._database.commit()

    def query(self, user_id: str, date: str) -> None | dict:
        self._cursor.execute(
            "select user_id, date, knife, loss from drop_log where user_id = ? and date = ?",
            (user_id, date)
        )
        result = self._cursor.fetchone()
        return None if result is None else wrap(result)
