from astrbot.api.all import Context

# 让 astrbot 的依赖安装器检测到
import cryptography
import wechatpy
import pydub

class Main:
    def __init__(self, context: Context) -> None:
        from .wecom_adapter import WecomPlatformAdapter # noqa
