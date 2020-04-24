import vk_api.vk_api
import numpy as np
from commander import Commander
from database import get_full_info
import random

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def get_rand():
    return np.int64(random.randint(0, 1000000000000))


class Server:
    def __init__(self, api_token, group_id, server_name: str = "Empty"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token=api_token)
        self.long_poll = VkBotLongPoll(self.vk, group_id)
        self.vk_api = self.vk.get_api()

        # Словарь для каждого отдельного пользователя
        self.users = {}

    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    def send_message(self, send_id, message):
        self.vk_api.messages.send(peer_id=send_id, message=message, random_id=get_rand())

    def send_to_subs(self):
        subs = get_full_info('mailinglist.csv')
        for row in subs:
            self.send_message(int(row[0]), 'Я проснулся!')

    def start(self):
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.from_id not in self.users:
                    self.users[event.object.message['from_id']] = Commander()
                if event.type == VkBotEventType.MESSAGE_NEW:
                    input_msg = self.users[event.object.message['from_id']].input(event.object.message['text'], event.object.message['from_id'],
                                                                         self.get_user_name(event.object.message['from_id']))
                    if input_msg != None:
                        self.send_message(event.object.message['peer_id'], input_msg)
