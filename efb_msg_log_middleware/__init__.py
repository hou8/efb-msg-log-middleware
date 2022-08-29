#coding=utf-8

import logging
from typing import Optional, Dict, Tuple
from ehforwarderbot.middleware import Middleware
from ehforwarderbot.message import Message
from ehforwarderbot.types import InstanceID, ModuleID
from .__version__ import __version__ as version


class MessageLogMiddleware(Middleware):
    middleware_id: str =  "hou8.msg_log"
    middleware_name: str = "Message Log Middleware"
    __version__: str = version

    def __init__(self, instance_id: Optional[InstanceID] = None):
        self.logger = logging.getLogger("hou8.msg_log")
        super().__init__(instance_id)

    def process_message(self, message: Message) -> Optional[Message]:
        self.logger.warn("msg: [%s]", message)
        return message
