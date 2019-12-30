import vk_api
import random
import os

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_bot import vkBot

token = os.environ.get('BOT_TOKEN')

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": random.randint(0, 1000)})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            # print('New message:')
            # print(f'For me by: {event.user_id}', end=' ')

            bot = vkBot(event.user_id)
            message = bot.new_msg(event.text)
            if isinstance(message, list):
                write_msg(event.user_id, 'Время | Предмет | Аудитория | Неделя')
                new_string = ''
                for row in message:
                    write_msg(event.user_id, str(row)[1:-1].replace(', None', '').replace(',', ' | '))
            else:
                write_msg(event.user_id, bot.new_msg(event.text))

            # print('Text: ', event.text)