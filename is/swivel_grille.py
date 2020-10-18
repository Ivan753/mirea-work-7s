"""
Программа для шифрации и дешифрации текста с помощью
метода поворотных решеток.

Шаблон задается заранее, проверки шаблона не производятся.
Порядок применения шаблона: по часовой стрелке

На кажом шаге алгоритма при шифрации и дешифрации выводится используемый шаблон
"""

"""
Получить новый шаблон
"""
def get_pattern_variant(pattern, n):
    if n == 0:
        return pattern

    k = len(pattern) if n%2 != 0 else len(pattern) // 2
    m = len(pattern[0]) // 2 if n%2 != 0 else len(pattern[0])

    for i in range(k):
        for j in range(m):
            temp = pattern[i][j]

            if n%2 != 0:
                pattern[i][j] = pattern[i][len(pattern[i]) - j - 1]
                pattern[i][len(pattern[i]) - j - 1] = temp
            else:
                pattern[i][j] = pattern[len(pattern) - i - 1][j]
                pattern[len(pattern) - i - 1][j] = temp

    return pattern

"""
Показать двумерную матрицу
"""
def print_matrix(matrix):
    print()

    for i in range(len(matrix)):
        print()
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")

"""
Шифрация
"""
def encode(pattern, text):
    text = list(text)

    result = [
        [" " for j in range(len(pattern[i]))]
        for i in range(len(pattern))
    ]

    for k in range(4):
        pattern = get_pattern_variant(pattern, k)

        print(f"\n\nШаблон для шага {k}:")
        print_matrix(pattern)

        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                if pattern[i][j] == 1:
                    if (len(text)):
                        result[i][j] = text.pop(0)
                    else:
                        return result
    return result


"""
Дешифрация
"""
def decode(pattern, matrix):
    result = ""
    for k in range(4):
        pattern = get_pattern_variant(pattern, k)

        print(f"\n\nШаблон для шага {k}:")
        print_matrix(pattern)

        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                if pattern[i][j] == 1:
                    result += matrix[i][j]
    return result


if __name__ == '__main__':
    # Исходные данные

    pattern = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]

    text = "ПРИВЕТ,МИР! ПИР!"


    # Шифрация
    print(f"Исходная строка: {text}")

    result = encode(pattern, text)

    print(f"\n\nРезульта шифрации:")
    print_matrix(result)

    # Дешифрация
    pattern = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ]

    result = decode(pattern, result)

    print(f"\n\nРезульта дешифрации:")
    print(result)
