"""
Одноразовый шифровальный блокнот

Запуск:
> python notepad_chiper.py "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.?! " "32 26 28 7 22 35 4 18 18 26 33 7" "ПИТЕР"

Или без параметров
"""

import sys


ALPHABET = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.?! ')


def get_number_by_char(char):
    return ALPHABET.index(char)


def get_char_by_number(number):
    return ALPHABET[number]


def encode(chars: list, key_list: list) -> str:
    result = []
    alphabet_len = len(ALPHABET)
    key_i = 0

    for char in chars:
        result.append(
            (
                get_number_by_char(char) + get_number_by_char(key_list[key_i])
            ) % alphabet_len
        )
        key_i += 1
        if key_i >= len(key_list):
            key_i = 0

    return " ".join(list(map(str, result)))


def decode(numbers: list, key_list: list) -> str:
    result = []
    alphabet_len = len(ALPHABET)
    key_i = 0

    for number in numbers:
        result.append(
            get_char_by_number(
                (number - get_number_by_char(key_list[key_i]))
                % alphabet_len
            )
        )
        key_i += 1
        if key_i >= len(key_list):
            key_i = 0

    return "".join(result)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        # декодирование
        # переопределяем алфавит
        ALPHABET = list(sys.argv[1])

        result = decode(list(map(int, sys.argv[2].split(" "))), sys.argv[3])

        print(result)

    else:
        # тестовый кейс
        init_str = "ПРИВЕТ, МИР!"
        key = "ПИТЕР"

        secret = encode(init_str, key)

        print(secret)

        result = decode(list(map(int, secret.split(" "))), key)

        print(result)
