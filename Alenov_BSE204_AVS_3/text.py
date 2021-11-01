import random
import rnd


class Text(object):
    # ------------------------------------------------------------------------------
    # Инициализация класса.
    def __init__(self):
        self.message = ""
        self.encrypted = ""
        self.quotient = 0.0

    # ------------------------------------------------------------------------------
    # Оверрайд сравнения классов.
    def __lt__(self, other):
        return self.quotient < other.quotient

    # ------------------------------------------------------------------------------
    # Метод заполнения поля частного.
    def get_quotient(self):
        sum = 0
        for i in self.message:
            sum += ord(i)

        self.quotient = sum * 1.0 / len(self.message)

    # ------------------------------------------------------------------------------
    # Заглушка метода шифрования.
    def encrypt(self):
        self.encrypted = self.message
        print("placeholder worked GL M8")

    # ------------------------------------------------------------------------------
    # Случайное заполнение текста.
    def in_rnd(self):
        rndmes = rnd.RndText()
        rndmes.get_rnd_text()
        self.message = rndmes.text_line
        self.encrypt()

    # ------------------------------------------------------------------------------
    # Метод вывода информации в файл.
    def out(self):
        return "Text: " + self.message + "\n"

    def __str__(self):
        return str(self.quotient)

