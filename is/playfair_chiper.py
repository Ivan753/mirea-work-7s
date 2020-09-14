import sys

class Chiper:

    alphabet = [
        'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
        'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Э', 'Ю', 'Я'
    ]

    m = []

    specialChar = 'А'

    def textToBigram(text):
        result = []
        ends = ""
        i = 0

        if len(text)%2 != 0:
            text += "А"

        while True:
            x1 = Chiper.replaceSymbol(text[i])
            x2 = Chiper.replaceSymbol(text[i+1])

            if x1 != x2:
                result.append([x1, x2])
                i += 2
            else:
                result.append([x1, Chiper.specialChar])
                i += 1

            if i >= len(text)-1:
                break
        return result


    def replaceSymbol(symbol):
        if symbol == 'Ь':
            symbol = 'Ъ'
        if symbol == 'Й':
            symbol = 'И'
        if symbol == 'Ё':
            symbol = 'Е'

        return symbol

    def generateMatrix(key):
        k = 0   # index for key
        a = 0   # index for alphabet

        for i in range(5):
            Chiper.m.append([])
            for j in range(6):
                if k < len(key):
                    symbol = key[k]
                    symbol = Chiper.replaceSymbol(symbol)

                    Chiper.m[i].append(symbol)
                    Chiper.alphabet.remove(symbol)
                    k += 1
                else:
                    Chiper.m[i].append(Chiper.alphabet[a])
                    a += 1

    def encode(text):
        result = []
        resultBigram = []
        i = 0   # index for text

        text = Chiper.textToBigram(text)

        for bigram in text:
            # get indexes of elements in matrix
            x1 = bigram[0]
            x2 = bigram[1]

            indexes = [[-1, -1], [-1, -1]]

            for j in range(len(Chiper.m)):
                line = Chiper.m[j]
                if x1 in line:
                    indexes[0] = [j, line.index(x1)]
                if x2 in line:
                    indexes[1] = [j, line.index(x2)]

            # calculate result bigram
            done = False
            ## rows
            if indexes[0][0] == indexes[1][0]:
                resultBigram = [
                    Chiper.m[indexes[0][0]][(indexes[0][1]+1)%6],
                    Chiper.m[indexes[1][0]][(indexes[1][1]+1)%6]
                ]
                done = True
            ## columns
            if indexes[0][1] == indexes[1][1]:
                resultBigram = [
                    Chiper.m[(indexes[0][0]+1)%5][indexes[0][1]],
                    Chiper.m[(indexes[1][0]+1)%5][indexes[1][1]]
                ]
                done = True
            ## else
            if not done:
                resultBigram = [
                    Chiper.m[indexes[0][0]][indexes[1][1]],
                    Chiper.m[indexes[1][0]][indexes[0][1]]
                ]

            result.append("".join(resultBigram))

        return "".join(result)


    def decode(text):
        result = []
        text = Chiper.textToBigram(text)

        print(Chiper.m)

        for bigram in text:
            # get indexes of elements in matrix
            x1 = bigram[0]
            x2 = bigram[1]

            indexes = [[-1, -1], [-1, -1]]

            for j in range(len(Chiper.m)):
                line = Chiper.m[j]
                if x1 in line:
                    indexes[0] = [j, line.index(x1)]
                if x2 in line:
                    indexes[1] = [j, line.index(x2)]

            # calculate result bigram
            done = False
            ## rows
            if indexes[0][0] == indexes[1][0]:
                resultBigram = [
                    Chiper.m[indexes[0][0]][(indexes[0][1]-1)%6],
                    Chiper.m[indexes[1][0]][(indexes[1][1]-1)%6]
                ]
                done = True
            ## columns
            if indexes[0][1] == indexes[1][1]:
                resultBigram = [
                    Chiper.m[(indexes[0][0]-1)%5][indexes[0][1]],
                    Chiper.m[(indexes[1][0]-1)%5][indexes[1][1]]
                ]
                done = True
            ## else
            if not done:
                resultBigram = [
                    Chiper.m[indexes[0][0]][indexes[1][1]],
                    Chiper.m[indexes[1][0]][indexes[0][1]]
                ]

            result.append("".join(resultBigram))
        return result


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 4:
        print("Неверное количество аргументов")
        exit()

    if (args[1] == "encode"):
        Chiper.generateMatrix(args[2])
        print(Chiper.encode(args[3]))
        exit()
    if (args[1] == "decode"):
        Chiper.generateMatrix(args[2])
        print(Chiper.decode(args[3]))
        exit()


