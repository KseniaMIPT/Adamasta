import argparse

parser = argparse.ArgumentParser(usage='Распечатывание файлов')
parser.add_argument('values', type=argparse.FileType('r'), nargs='+', help='файлы, которые требуется распечатать')
args = parser.parse_args()

for file in args.values:
    print(file.read())
    file.close()
