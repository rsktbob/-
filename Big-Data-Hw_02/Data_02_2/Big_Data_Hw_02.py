# 使用python將names-10000.txt加以整理和加入id,score最後產生data.txt，將data.txt是grade.sql的重要資料，
# grade.sql裡的指令可以完成此次作業，image的資料夾有題目的結果

import random


def check_range(num):
    if num < 0:
        return 0
    elif num > 100:
        return 100
    return num


with open('names-10000.txt', 'r', encoding='utf-8') as f:
    name = f.read()

name = name.split(', ')
data = ''
padding = 7

for i in range(10000):
    data += f'(\'{i+1:0>{padding}}\', \'{name[i]}\', '
    for j in range(4):
        data += f'{int(check_range(random.gauss(50, 25)))}, '
    if i != 9999:
        data += f'{int(check_range(random.gauss(50, 25)))}),\n'
    else:
        data += f'{int(check_range(random.gauss(50, 25)))});'

with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(data)
