from command_enum import Command
from mode_enum import Mode
from talking import BotTalk
import random

# Рабочие модули
from myanimelist import Myanimelist

talk = BotTalk()


class Commander:
    def __init__(self):

        # Текущий, предыдущий режимы
        self.now_mode = Mode.default
        self.last_mode = Mode.default

        self.last_command = None

        # Для запомминания ответов пользователя
        self.last_ans = None

    def change_mode(self, to_mode):
        """
        Меняет режим приема команд
        :param to_mode: Измененный мод
        """
        self.last_mode = self.now_mode
        self.now_mode = to_mode

        self.last_ans = None

    def input(self, msg, person_id, username):
        """
        Функция принимающая сообщения пользователя
        :param msg: Сообщение
        :return: Ответ пользователю, отправившему сообщение
        """
        """
        # Проверка на команду смены мода
        if msg.startswith("$"):
            for mode in Mode:
                if msg[1::] in mode.value:
                    self.change_mode(mode)
                    return "Режим изменен на " + self.now_mode.value[0]
            return "Неизвестный мод " + msg[1::]
        """
        # Режим получения ответа
        if self.now_mode == Mode.get_ans:
            self.last_ans = msg
            self.now_mode = self.last_mode
            return "Ok!"

        if self.now_mode == Mode.default:

            # Топ аниме
            if msg in Command.anime_top.value:
                res = ""
                top = Myanimelist.get_top()
                for anime in top:
                    res += anime + " : " + top[anime] + "\n"

                return res

            if msg in Command.whoami.value and person_id == 233908651:
                return "Ты мой разработчик и говно-("
            elif msg in Command.whoami.value:
                return "Ты говно-("

            # Болталка
            if msg in Command.hello_msg.value:
                return talk.input(1)

            if msg in Command.how_msg.value:
                return talk.input(2)

            if msg in Command.bye_msg.value:
                return talk.input(3)

            if msg in Command.morn_msg.value:
                return talk.input(4)

            # Насколько ты гей
            if msg in Command.how_many_gay.value:
                return "[id" + str(person_id) + "|" + username + "]," + " ты гей на " + str(random.randint(0, 100)) + "%"


        return None
