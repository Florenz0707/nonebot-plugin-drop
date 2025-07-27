import datetime


def get_today_str() -> str:
    return datetime.datetime.now().strftime("%y%m%d")


def wrap(info: tuple | list) -> dict:
    keys = ('user_id', 'date', 'knife', 'loss')
    return {key: val for key, val in zip(keys, info)}
