"""
Napisz program do generowania losowych haseł o zadanej przez użytkownika długości. Hasło musi spełniać zadane warunki
 np. co najmniej jedna liczba, co najmniej po jednej dużej i małej literze. Warto skorzystać z modułów string i secrets.
Propozycja rozszerzenia: Po wygenerowaniu hasła skopiuj je do schowka systemowego 🙂"""

import string
import secrets
import pyperclip


class TooShortLength(Exception):
    pass


class PasswordGenerator:
    def __init__(self, length):
        """
        :param length: length of requested password
        """
        self.length = length

    def create_password(self):
        """
        create password from alphabet + digits and uppercases
        :return: 
        """
        alphabet = string.ascii_letters+string.digits+string.ascii_uppercase
        return "".join(secrets.choice(alphabet) for i in range(self.length+1))

    def check_correctness(self):
        """
        check correctness of create password
        :return:
        """
        password = self.create_password()
        if (any(word.islower() for word in password) and
            any(word.isupper() for word in password) and
            any(word.isdigit() for word in password)):
            return password
        else:
            self.check_correctness()

    @property
    def password(self):
        return self.check_correctness()


def main():
    while True:
        try:
            length = int(input('Please provide password length (should be longer than 8):'))
        except ValueError:
            print("Could not convert data to an integer.")
        else:
            if length >8:
                new = PasswordGenerator(length)
                #copy to clipboard
                pyperclip.copy(str(new.password))
                print(f'Your new password {new.password} copied to clipboard')
            else:
                print('We can not create unsafe password')


if __name__ == '__main__':
    main()
