"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

yan = ['ping', 'yandex.ru']
you = ['ping', 'youtube.com']
yan_ping = subprocess.Popen(yan, stdout=subprocess.PIPE)
you_ping = subprocess.Popen(yan, stdout=subprocess.PIPE)

for line in yan_ping.stdout:
    char = chardet.detect(line)
    lin = line.decode(char['encoding']).encode('utf-8')
    print(lin.decode('utf-8'))


for line in you_ping.stdout:
    char = chardet.detect(line)
    lin = line.decode(char['encoding']).encode('utf-8')
    print(lin.decode('utf-8'))
