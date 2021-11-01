import text
import random


class CyclicShift(text.Text):
    n = 0

    # ------------------------------------------------------------------------------
    # Метод шифрования.
    def encrypt(self):
        self.encrypted += "(n = " + str(self.n) + ") "
        for i in self.message:
            if i == ' ':
                self.encrypted += ' '
            else:
                self.encrypted += chr(ord(i) + self.n)
        # Заполняем значение частного.
        self.get_quotient()

    # ------------------------------------------------------------------------------
    # Метод случайного шифрования.
    def encrypt_rnd(self):
        self.n = random.randint(1, 8)
        self.encrypted += "(n = " + str(self.n) + ") "
        for i in self.message:
            if i == ' ':
                self.encrypted += ' '
            else:
                self.encrypted += chr(int(i) + self.n)
        # Заполняем значение частного.
        self.get_quotient()

    # ------------------------------------------------------------------------------
    # Метод вывода информации в файл.
    def out(self):
        return "\n  Text: " + self.message + "\n  Encryption by cyclically shifting the code of each character by " + str(
            self.n) + ": " + self.encrypted + "\n"

    def __str__(self):
        return str(self.quotient)
