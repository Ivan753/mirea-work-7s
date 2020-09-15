import sys

class Chiper:

    alphabet = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
        'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
    ]

    def encode(text, offset):
        result = ""

        for a in text:
            result += Chiper.alphabet[(Chiper.alphabet.index(a)+offset)%len(Chiper.alphabet)]

        return result


    def decode(text, offset):
        result = ""

        for a in text:
            result += Chiper.alphabet[(Chiper.alphabet.index(a)-offset)%len(Chiper.alphabet)]

        return result


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 4:
        print("Неверное количество аргументов")
        exit()

    if (args[1] == "encode"):
        print(Chiper.encode(args[3], int(args[2])))
        exit()

    if (args[1] == "decode"):
        print(Chiper.decode(args[3], int(args[2])))
        exit()

    if (args[1] == "superdecode"):
        for i in range(32):
            print(Chiper.decode(args[3], i), i)

