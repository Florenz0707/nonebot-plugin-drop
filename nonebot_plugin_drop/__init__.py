# ------------------------ import ------------------------
# import packages from python
import random

# import packages from nonebot or other plugins
from nonebot import require
from nonebot.log import logger

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import *

require("nonebot_plugin_uninfo")
from nonebot_plugin_uninfo import *

from .Database import Database
from .Loader import Loader
from .utils import get_today_str, wrap, get_quality

# ------------------------ import ------------------------

__plugin_meta__ = PluginMetadata(
    name="",
    description="",
    usage="""
    """,
    homepage="https://github.com/Florenz0707/nonebot-plugin-drop",
    type="application",
    config=Config,
    supported_adapters={"~onebot.v11"},
    extra={
        "author": "florenz0707",
    }
)

database = Database()
loader = Loader()
items = loader.get_items()

drop = on_alconna("drop", use_cmd_start=True)


@drop.handle()
async def drop_handler(session: Uninfo):
    user_id = session.user.id
    today_str = get_today_str()
    if (info := database.query(user_id, today_str)) is None:
        knife = random.choice(items)
        loss = random.random()
        database.insert(user_id, today_str, knife, loss)
        info = database.query(user_id, today_str)

    message = UniMessage.text("\n队友给你发了一把").image(
        path=loader.get_item_path(info.get('knife'))).text(
        f"{info.get('knife').replace('-', ' | ')}\n"
        f"{get_quality(info.get('loss'))}（{info.get('loss'): .4f}）"
    )
    await message.finish(at_sender=True)
