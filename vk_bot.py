from database import get_connection


class vkBot:

    def __init__(self, user_id):
        self.user_id = user_id

        self.commands = ['расписание']
        self.hello_message = ['привет', 'здравствуйте', 'приветствую']
        self.goodbye_message = ['пока', 'удачи', 'увидимся', 'спасибо']

    def new_msg(self, message):
        if message.lower() in self.hello_message:
            return "Привет, меня зовут Планктон\n Напиши номер своей группы и получишь расписание\n Например '8391'"
        elif message.lower() in self.goodbye_message:
            return "Успехов тебе!"
        else:
            try:
                msg = int(message)
                info = get_connection(msg)
                return info
            except:
                return 'Что-то я тебя не понимаю\nПопробуй еще раз :-)'

