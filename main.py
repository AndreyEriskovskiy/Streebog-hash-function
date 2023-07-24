from operations import streebog_256_512
import sys

mode = input('Способ ввода текста (1 - ввод строки, 2 - текстовый файл): ')

if mode == '1':
    text = input('Входной текст: ')

elif mode == '2':
    filename = input('Путь к файлу: ')

    try:
        with open(filename, encoding='utf-8') as f:
            text = f.read()


    except FileNotFoundError:
        print('Файл не найден')
        sys.exit(0)

    except:
        print('Ошибка открытия файла')
        sys.exit(0)




M = ''

for code in [ord(char) for char in text]:
    M += hex(code)[2:].zfill(4)



if __name__ == '__main__':

    hash_512 = streebog_256_512(M, '1')
    hash_256 = streebog_256_512(M, '2')
    print(f'''Хэш-код 512 bit: {hash_512}
Хэш-код 256 bit: {hash_256}''')


    
