import argparse
from os import path, listdir

parser = argparse.ArgumentParser(description='Программа, отображающая древовидную структуру каталогов и файлов.')

parser.add_argument('values', metavar='VALUES', type=str, nargs='+',
                    help='путь к каталогу, чья структура будет отображена')

parser.add_argument('-f', '--folders_only', action="store_true", help='не отображать файлы в дереве')
parser.add_argument('-i', '--include', metavar='ACTION', action="store",
                    help='отображать только те элементы, в названии которых встречается текст')
parser.add_argument('-e', '--exclude', metavar='ACTION', action="store",
                    help='не отображать те элементы, в названии которых встречается текст')

args = parser.parse_args()

names = args.values

for name in names:
    if not path.isdir(name):
        print("Указанный путь не существует или не является папкой - " + name)
        exit()


def tree(name, x=0):
    if (args.folders_only and path.isfile(name)) and name is not None:  # FIXME
        return None
    if name is not None:
        print('   ' * x + name)
        if path.isdir(name):
            name_list = listdir(name)
            x += 1
            for i in range(len(name_list)):
                tree(name_list[i], x)


for name in names:
    tree(name, -1)
