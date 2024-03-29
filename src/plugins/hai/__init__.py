import nonebot

from nonebot import on_regex
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.permission import Permission, SUPERUSER

from .config import Config

cfg = Config()
print(cfg.regex)
aha = on_regex(cfg.regex)


@aha.handle()
async def hai(bot: Bot, event: Event, state: T_State):
    await aha.send(event.get_message())


