import sys

try:
    raio = float(input('Informe o Raio: '))
except ValueError:
    print('Foi informado um valor não numérico...')
except:
    print('Erro Inesperado...', sys.exc_info())
else:
    if (raio > 0):
        pi = 3.14
        area = pi * raio * raio
        comprimento = 2 * pi * raio
        print('O Comprimento da Circunferência é', comprimento)
        print('A Área do Círculo é', area)
    else:
        print('Informe um raio positivo...')