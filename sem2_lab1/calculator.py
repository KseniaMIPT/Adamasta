import argparse
import sys

parser = argparse.ArgumentParser(description='Консольный калькулятор')

parser.add_argument('values', metavar='VALUES', type=float, nargs='+',
                    help='числа, над которыми требуется выполнить действия')

parser.add_argument('-a', '--action', metavar='ACTION', action='store', help='выполнить арифметическую операцию')
parser.add_argument('-v', '--verbose', metavar='ACTION', action='store',
                    help='вывод самого вычисляемого выражения со знаком равенства перед ответом')

args = parser.parse_args()

if not args.action and not args.verbose:
    print('Должен быть указан один из параметров --action и --verbose', file=sys.stderr)
    sys.exit(-1)

x = float(args.values[0])
y = float(args.values[-1])
z = float()

if args.action:
    if args.action == '+':
        z = x + y
        print(z)
    elif args.action == '-':
        z = x - y
        print(z)
    elif args.action == '*':
        z = x * y
        print(z)
    elif args.action == '/':
        z = x / y
        print(z)
    else:
        print('Неверный знак операции', file=sys.stderr)
        sys.exit(-1)

if args.verbose:
    if args.verbose == '+':
        z = x + y
        print(x, args.verbose, y, '=', z)
    elif args.verbose == '-':
        z = x - y
        print(x, args.verbose, y, '=', z)
    elif args.verbose == '*':
        z = x * y
        print(x, args.verbose, y, '=', z)
    elif args.verbose == '/':
        z = x / y
        print(x, args.verbose, y, '=', z)
    else:
        print('Неверный знак операции', file=sys.stderr)
        sys.exit(-1)
