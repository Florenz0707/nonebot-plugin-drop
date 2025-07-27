import datetime

quality = (
    (0.07, "崭新出厂"),
    (0.15, "略有磨损"),
    (0.38, "久经沙场"),
    (0.45, "破损不堪"),
    (0.80, "战痕累累"),
    (1.00, "废弃物品")
)


def get_today_str() -> str:
    return datetime.datetime.now().strftime("%y%m%d")


def wrap(info: tuple | list) -> dict | None:
    if len(info) != 4:
        return None
    keys = ('user_id', 'date', 'knife', 'loss')
    return {key: val for key, val in zip(keys, info)}


def get_quality(loss: float) -> str:
    for val, res in quality:
        if loss <= val:
            return res
    return "ERROR"
