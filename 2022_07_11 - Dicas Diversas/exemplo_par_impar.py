#! C:/Users/charl/AppData/Local/Programs/Python/Python310

import sys

print(sys.argv)

try:
    if len(sys.argv) == 1:
        valor_x = int(input('Informe um número: '))
    else:
        valor_x = int(sys.argv[1])
except ValueError:
    print(f'ERRO....: Informe um valor INTEIRO')
except:
    print(f'ERRO....: {sys.exc_info()[0]}')
else:
    if (valor_x % 2 == 0):
        print(f'O valor {valor_x} é PAR...')
    else:
        print(f'O valor {valor_x} é ÍMPAR...')