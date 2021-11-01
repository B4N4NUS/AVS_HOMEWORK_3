import text


class CharecterReplacement(text.Text):
    # ------------------------------------------------------------------------------
    # Метод шифрования.
    def encrypt(self):
        # Изначальный алфавит.
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # Алфавит для шифровки.
        encrypt_code = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        for i in self.message:
            if i == ' ':
                self.encrypted += " "
            elif alphabet.find(i) is not None:
                self.encrypted += encrypt_code[alphabet.find(i)]
            else:
                self.encrypted += i
        # Заполняем значение частного.
        self.get_quotient()

    # ------------------------------------------------------------------------------
    # Метод вывода информации в файл.
    def out(self):
        return "\n  Text: " + self.message + "\n  Encryption by substitution of characters: " + self.encrypted + "\n"

    def __str__(self):
        return str(self.quotient)
