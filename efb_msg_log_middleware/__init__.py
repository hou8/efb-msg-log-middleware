# coding=utf-8

from datetime import datetime
import json
import logging
import os
from pathlib import Path
from typing import Optional

from ehforwarderbot import utils
from ehforwarderbot.message import Message
from ehforwarderbot.middleware import Middleware
from ehforwarderbot.types import InstanceID, ModuleID

from .__version__ import __version__ as version


def msg2dic(msg: Message):
    if isinstance(msg, Message):
        return dict(
            # Message
            uid=msg.uid,
            type=msg.type.value,
            text=msg.text,
            edit=msg.edit,
            edit_media=msg.edit_media,
            filename=msg.filename,
            is_system=msg.is_system,
            mime=msg.mime,
            path=msg.path,
            target_uid=None if msg.target is None else msg.target.uid,
            # Chat
            chat_id=msg.chat.id,
            chat_uid=msg.chat.uid,
            chat_name=msg.chat.name,
            chat_descption=msg.chat.description,
            chat_module_id=msg.chat.module_id,
            chat_module_name=msg.chat.module_name,
            chat_channel_emoji=msg.chat.channel_emoji,
            # ChatMember(author)
            author_id=msg.author.id,
            author_uid=msg.author.uid,
            author_name=msg.author.name,
            author_alias=msg.author.alias,
            author_description=msg.author.description,
            # Channel(deliver_to)
            deliver_to_channel_id=msg.deliver_to.channel_id,
            deliver_to_channel_name=msg.deliver_to.channel_name,
            deliver_to_channel_emoji=msg.deliver_to.channel_emoji,
            deliver_to_instance_id=msg.deliver_to.instance_id,
        )
    else:
        return msg


class MessageLogMiddleware(Middleware):
    middleware_id: ModuleID = ModuleID("hou8.msg_log")
    middleware_name: str = "Message Log Middleware"
    __version__: str = version

    def __init__(self, instance_id: Optional[InstanceID] = None):
        self.logger = logging.getLogger("hou8.msg_log")
        storage_path = utils.get_data_path(self.middleware_id)
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        super().__init__(instance_id)

    def process_message(self, message: Message) -> Optional[Message]:
        with open(self._log_path(), 'a') as file:
            json.dump(message, file, default=msg2dic, ensure_ascii=False)
            file.write('\n')
        return message

    def _log_path(self) -> Path:
        storage_path = utils.get_data_path(self.middleware_id)
        date_str = datetime.now().strftime("%Y%m")
        return storage_path.joinpath(f'{date_str}_log.json')
