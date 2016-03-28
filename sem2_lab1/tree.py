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
    if name is not None:
        print('   ' * x + name)
        if path.isdir(name):
            name_list = listdir(name)
            if args.folders_only:
                name_list = [name for name in name_list if path.isdir(name)]
            if args.include:
                name_list = [name for name in name_list if args.include in name]
            if args.exclude:
                name_list = [name for name in name_list if not (args.exclude in name)]
            x += 1
            for name in name_list:
                tree(name, x)

for name in names:
    tree(name, -1)
