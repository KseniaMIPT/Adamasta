from sys import argv

if len(argv) < 2:
    print('Введите имя хотя бы одного файла')

for name in argv[1:]:
    file = open(name, 'r')
    print(file.read())
    file.close()
