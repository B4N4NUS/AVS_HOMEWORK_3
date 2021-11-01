import text


class CharecterToNumber(text.Text):
    # ------------------------------------------------------------------------------
    # Метод шифрования.
    def encrypt(self):
        for i in self.message:
            if i == ' ':
                self.encrypted += "/ "
            else:
                self.encrypted += str(ord(i)) + " "
        # Заполняем значение частного.
        self.get_quotient()

    # ------------------------------------------------------------------------------
    # Метод вывода информации в консоль.
    def out(self):
        return "\n  Text: " + self.message + "\n  Encryption by replacing characters with numbers: " + self.encrypted + "\n"

    def __str__(self):
        return str(self.quotient)
