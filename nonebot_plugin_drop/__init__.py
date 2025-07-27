# ------------------------ import ------------------------
# import packages from python
import os
import random

from nonebot import require
from nonebot.adapters.onebot.v11 import Bot
from nonebot.log import logger
# import packages from nonebot or other plugins
from nonebot.permission import Permission, SUPERUSER, SuperUser, Event

require("nonebot_plugin_alconna")
from nonebot_plugin_alconna import *

require("nonebot_plugin_uninfo")
from nonebot_plugin_uninfo import *

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
