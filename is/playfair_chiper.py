import sys

class Chiper:

    """
    Инифиализация изменяющегося для матрицы алфавита
    и неизменяющегося для проверки алфавита,
    списка для матрицы и специального символа (вставляется, если биграмма содержит два одинаковых символа)
    """
    def __init__(self):
        self.alphabet = [
            'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Э', 'Ю', 'Я'
        ]

        self.m = []
        self.specialChar = 'А'

    """
    Перевод текста в биграммы
    """
    def textToBigram(self, text):
        result = []
        ends = ""
        i = 0

        if len(text)%2 != 0:
            text += "А"

        while True:
            x1 = self.replaceSymbol(text[i])
            x2 = self.replaceSymbol(text[i+1])

            if x1 != x2:
                result.append([x1, x2])
                i += 2
            else:
                result.append([x1, self.specialChar])
                i += 1

            if i >= len(text)-1:
                break
        return result


    """
    Смена символов для соответствия алфавиту
    """
    def replaceSymbol(self, symbol):
        if not symbol in self.alphabet:
            print("Incorrect symbol ", symbol)
            exit()

        if symbol == 'Ь':
            return 'Ъ'
        elif symbol == 'Й':
            return 'И'
        elif symbol == 'Ё':
            return 'Е'

        return symbol

    """
    Генерация матрицы
    """
    def generateMatrix(self, key):
        k = 0   # index for key
        a = 0   # index for alphabet

        copyAlphabet = self.alphabet.copy()

        for i in range(5):
            self.m.append([])
            for j in range(6):
                if k < len(key):
                    symbol = self.replaceSymbol(key[k])

                    self.m[i].append(symbol)
                    copyAlphabet.remove(symbol)
                    k += 1
                else:
                    self.m[i].append(copyAlphabet[a])
                    a += 1

    def getIndexesOfChar(self, x):
        indexes = [-1, -1]

        for j in range(len(self.m)):
            line = self.m[j]
            if x in line:
                indexes = [j, line.index(x)]
        return indexes

    def encode(self, text):
        result = []
        resultBigram = []
        i = 0   # index for text

        text = self.textToBigram(text)

        for bigram in text:
            # get indexes of elements in matrix
            x1 = bigram[0]
            x2 = bigram[1]

            indexes = [
                self.getIndexesOfChar(x1),
                self.getIndexesOfChar(x2),
            ]

            # calculate result bigram
            done = False
            ## rows
            if indexes[0][0] == indexes[1][0]:
                resultBigram = [
                    self.m[indexes[0][0]][(indexes[0][1]+1)%6],
                    self.m[indexes[1][0]][(indexes[1][1]+1)%6]
                ]
                done = True
            ## columns
            if indexes[0][1] == indexes[1][1]:
                resultBigram = [
                    self.m[(indexes[0][0]+1)%5][indexes[0][1]],
                    self.m[(indexes[1][0]+1)%5][indexes[1][1]]
                ]
                done = True
            ## else
            if not done:
                resultBigram = [
                    self.m[indexes[0][0]][indexes[1][1]],
                    self.m[indexes[1][0]][indexes[0][1]]
                ]

            result.append("".join(resultBigram))

        return "".join(result)


    def decode(self, text):
        result = []
        text = self.textToBigram(text)

        print(self.m)

        for bigram in text:
            # get indexes of elements in matrix
            x1 = bigram[0]
            x2 = bigram[1]

            indexes = [
                self.getIndexesOfChar(x1),
                self.getIndexesOfChar(x2),
            ]

            # calculate result bigram
            done = False
            ## rows
            if indexes[0][0] == indexes[1][0]:
                resultBigram = [
                    self.m[indexes[0][0]][(indexes[0][1]-1)%6],
                    self.m[indexes[1][0]][(indexes[1][1]-1)%6]
                ]
                done = True
            ## columns
            if indexes[0][1] == indexes[1][1]:
                resultBigram = [
                    self.m[(indexes[0][0]-1)%5][indexes[0][1]],
                    self.m[(indexes[1][0]-1)%5][indexes[1][1]]
                ]
                done = True
            ## else
            if not done:
                resultBigram = [
                    self.m[indexes[0][0]][indexes[1][1]],
                    self.m[indexes[1][0]][indexes[0][1]]
                ]

            result.append("".join(resultBigram))
        return result


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 4:
        print("Неверное количество аргументов")
        exit()

    chiper = Chiper()

    if (args[1] == "encode"):
        chiper.generateMatrix(args[2])
        print(chiper.encode(args[3]))
        exit()
    if (args[1] == "decode"):
        chiper.generateMatrix(args[2])
        print(chiper.decode(args[3]))
        exit()
