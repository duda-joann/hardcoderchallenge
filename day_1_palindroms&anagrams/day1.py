import webbrowser


class Palindrom:
    def __init__(self, expression):
        self.expression = expression.lower()

    def format_word(self):
        return "".join([word for word in self.expression if word.isalpha()])

    def reverse_word(self):
        word = self.format_word()
        return word[::-1]

    def is_palindrom(self):
        word = self.format_word()
        reverse = self.reverse_word()
        return word == reverse


def main():
    while True:
        user_input = input('Give your word:')
        print(user_input)
        word = Palindrom(user_input)
        reversed = word.reverse_word()
        print(reversed)
        print(word.is_palindrom())
        url = f'https://poocoo.pl/scrabble-slowa-z-liter/{user_input}'
        webbrowser.open(url)
        action = input("do you want continue: [y/n]: ")
        if action == 'n':
            break


if __name__ == '__main__':
    main()


