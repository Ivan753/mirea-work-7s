"""
Дешифрация текста, полученного применением шифра "Лесенка"
к исходному тексту
Аргументы: <начальное количество ступеней> <конечное количество ступеней> <текст>
"""
import sys


if __name__ == '__main__':
    args = sys.argv

    if len(args) < 3:
        raise Exception("Неверное количество аргументов")

    text = list(
      args[3]
    )

    start = int(args[1])
    finish = int(args[2])


    for i in range(start, finish):
        splittedText = []
        # получаем длину ступени без остатка
        partsLength = len(text) // i
        # смотрим, нужен ли остаток (добавляется по единице к строке, пока остаток не закончится)
        add = 0
        if (len(text)%i > 0):
            add = 1

        k = 0 # текущий начальный символ, идентифицирубщий новую ступень
        for j in range(i):
            # если новер ступени превышает остаток, то единица не добавляется
            if k // partsLength >= len(text)%i:
                add = 0

            splittedText.append(text[k:k+partsLength+add])
            k = k + partsLength + add

        print()
        print()
        print(str(i)+".", end=" ")
        for ii in range(len(splittedText[0])):
            for jj in range(len(splittedText)):
                if (ii >= len(splittedText[jj])):
                    continue

                print(splittedText[jj][ii], end=" ")
