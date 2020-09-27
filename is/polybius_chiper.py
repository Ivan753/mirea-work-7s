import sys

class Chiper:

    def __init__(self):
        self.alphabet = [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Э', 'Ю', 'Я'
        ]

        self.matrix = [
            self.alphabet[:6],
            self.alphabet[6:12],
            self.alphabet[12:18],
            self.alphabet[18:24],
            self.alphabet[24:30]
        ]


    def getIndexesOfChar(self, x):
        for j in range(len(self.matrix)):
            line = self.matrix[j]
            if x in line:
                return [str(j), str(line.index(x))]

    def getCharViaIndexes(self, indexes):
        return self.matrix[indexes[0]][indexes[1]]

    def stringToChars(self, string):
        return [char for char in string]

    def do(self, command, text):
        result = []

        chars = self.stringToChars(text)
        i = 0

        while True:
            if i >= len(chars):
                break

            if command == "encode":
                indexes = self.getIndexesOfChar(chars[i])
                result.append("".join(indexes))
                i = i + 1
            elif command == "decode":
                char = self.getCharViaIndexes([int(chars[i]), int(chars[i+1])])
                result.append(char)
                i = i + 2
            else:
                raise Exception("Incorrect command (encode, decode)")


        return "".join(result)

if __name__ == '__main__':
    args = sys.argv

    if len(args) < 3:
        raise Exception("Неверное количество аргументов")

    print(Chiper().do(args[1], args[2]))
