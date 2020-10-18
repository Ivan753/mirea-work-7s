"""
Программа для шифрации и дешифрации текста в изображении
формата BMP
Используются только ASCII символы размером в 1 байт (8 бит)
"""


from PIL import Image


SYMBOL_SIZE = 8

def encode(image_src, text):
    src_image = Image.open(image_src)

    # используемый цвет (0 - r, 1 - g, 2 - b)
    current_color = 0

    # размеры изображения
    src_width, src_height = src_image.size

    # посчитанные символы
    count = 0

    # счет для битов символа
    symbol_count = 0

    # маска для выборки бита крайнего разряда
    mask = 2**(SYMBOL_SIZE-1)

    for j in range(src_height):
        if count >= len(text):
            break
        for i in range(src_width):
            for k in range(3):
                pixel = list(src_image.getpixel((i, j)))

                bit = bool((ord(text[count])<<symbol_count)&mask)

                if (pixel[current_color]%2 == 0 and bit) or (pixel[current_color]%2 == 1 and not bit):
                    pixel[current_color] = (pixel[current_color]+1)%256

                current_color = current_color+1 if current_color < 2 else 0

                src_image.putpixel((i, j), tuple(pixel))

                # пересчет счетчиков
                symbol_count += 1
                if symbol_count == SYMBOL_SIZE:
                    symbol_count = 0
                    count += 1
                    if count >= len(text):
                        break
            if count >= len(text):
                break

    new_image_path = f"{image_src.partition('.')[0]}_enc.bmp"
    src_image.save(new_image_path)


def decode(image_src, length):
    src_image = Image.open(image_src)

    # размеры изображения
    src_width, src_height = src_image.size

    # посчитанные символы
    count = 0

    # счет для генерации символа
    symbol_count = 0

    symbol_text = ""

    symbols = []

    for j in range(src_height):
        for i in range(src_width):
            pixel = list(src_image.getpixel((i, j)))

            for color_id in range(3):
                symbol_count += 1
                if pixel[color_id] %2 == 0:
                    symbol_text += "0"
                else:
                    symbol_text += "1"

                if symbol_count == SYMBOL_SIZE:
                    symbol_count = 0
                    symbols.append(chr(int(symbol_text, 2)))
                    symbol_text = ""
                    count += 1
                    if count >= length:
                        return symbols
    return symbols


if __name__ == "__main__":
    # создает изображение, в которое закодировано 13 символов
    encode("dummy/test.bmp", "Hello, world!")

    # считываем изображение, декодируя первые 13 символов
    result = decode("dummy/test_enc.bmp", 13)
    print("".join(result))
