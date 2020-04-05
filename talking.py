import random
"""
mode:
1 - привет
2 - как дела
3 - пока
"""

class BotTalk:
    def __init__(self):
        self.hello_qts = ["Привет!", "Здравствуй брух", "Hello world!"]
        self.how_qts = ["Отлично!", "Ужасно(", "У меня дел не бывает"]
        self.bye_qts = ["Пока пока", "Пока \nБрух...", "Ну и пиздуй"]

    def input(self, mode):
        if mode == 1:
            ind = random.randint(0, len(self.hello_qts) - 1)
            return self.hello_qts[ind]
        if mode == 2:
            ind = random.randint(0, len(self.how_qts) - 1)
            return self.how_qts[ind]
        if mode == 3:
            ind = random.randint(0, len(self.bye_qts) - 1)
            return self.bye_qts[ind]
        return 'A?'

