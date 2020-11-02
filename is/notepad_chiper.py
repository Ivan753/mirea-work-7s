"""
Одноразовый шифровальный блокнот

Запуск:
# для шифрации и дешифрации
> python notepad_chiper.py chat "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.?! " "788,33,745,259,109,397,506,747,221,48,653,445,834,847,50,313,444,491;405,526,970,66,945,930,474,555,609,78,27,256"

# для генерации ключей
> python notepad_chiper.py generate 2

Или без параметров для теста encode\decode:
> python notepad_chiper.py
"""


import sys
import random

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
                    get_number_by_char(char) + int(key_list[key_i])
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
                (number - int(key_list[key_i]))
                % alphabet_len
            )
        )
        key_i += 1
        if key_i >= len(key_list):
            key_i = 0

    return "".join(result)


def generate_keys(count: int) -> str:
    keys = []

    for _ in range(count):
        key_len = random.randint(10, 20)
        key = [str(random.randint(0, 1000)) for i in range(key_len)]
        keys.append(",".join(key))

    return ";".join(list(map(str, keys)))


def go(keys_str: str) -> None:
    keys = keys_str.split(";")

    print("Commands:")
    print("\en - encode text")
    print("\dec - decode text")
    print("\s - next page")
    print("\q - exit")

    while True:
        command = input()
        key = keys[0].split(",")

        if command == "\en":
            text = input("Enter text for encoding:\n")

            print("Result encoding")
            print(encode(list(text), key))
        elif command == "\dec":
            secret_text = input("Enter text for decoding:\n")

            print("Result decoding")
            print(decode(list(map(int, secret_text.split(" "))), key))

        elif command == "\s":
            keys.pop(0)

            if not len(keys):
                print("The end")
                exit(0)
        elif command == "\q":
            print("Exit from chiper")

            print("Remaining keys")
            print(";".join(keys))

            exit(0)
        else:
            print("Unrecognized command")


if __name__ == '__main__':

    if len(sys.argv) > 1:

        if sys.argv[1] == "generate":
            print(generate_keys(int(sys.argv[2])))
        elif sys.argv[1] == "chat":
            ALPHABET = list(sys.argv[2])
            print(go(sys.argv[3]))

        exit()

        # декодирование
        # переопределяем алфавит
        # ALPHABET = list(sys.argv[1])
        #
        # result = decode(list(map(int, sys.argv[2].split(" "))), sys.argv[3])
        #
        # print(result)

    else:
        # тестовый кейс
        init_str = "ПРИВЕТ, МИР!"
        key = "788,33,745,259,109,397,506,747,221,48,653".split(",")

        secret = encode(init_str, key)

        print(secret)

        result = decode(list(map(int, secret.split(" "))), key)

        print(result)
