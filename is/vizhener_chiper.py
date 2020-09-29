import sys

class Chiper:

    def __init__(self):
        self.alphabet = [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Э', 'Ю', 'Я', ',', '.', '_'
        ]

    def generateKeyStr(self, keyword, ll):
        result = []

        for i in range(ll):
            result.append(keyword[i%len(keyword)])

        return "".join(result)

    def do(self, command, keyword, text):
        result = []

        keyString = self.generateKeyStr(keyword, len(text))

        for i in range(len(text)):
            if command == "encode":
                index = (self.alphabet.index(keyString[i]) + self.alphabet.index(text[i]))%(len(self.alphabet))
            elif command == "decode":
                index = (self.alphabet.index(text[i]) - self.alphabet.index(keyString[i]))
                index = index + len(self.alphabet) if index < 0 else index

            result.append(self.alphabet[index])

        return "".join(result)

if __name__ == '__main__':
    args = sys.argv

    if len(args) < 4:
        raise Exception("Неверное количество аргументов")

    print(Chiper().do(args[1], args[2], args[3]))
