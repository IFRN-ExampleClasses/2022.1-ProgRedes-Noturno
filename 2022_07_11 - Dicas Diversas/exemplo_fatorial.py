import sys

print(sys.argv)

try:
    if len(sys.argv) == 1:
        valor = int(input('Informe um número: '))
    else:
        valor = int(sys.argv[1])
    valor_informado = valor
except ValueError:
    print(f'ERRO....: Informe um valor INTEIRO')
except:
    print(f'ERRO....: {sys.exc_info()[0]}')
else:
    if (valor == 1) or (valor == 0):
        print(f'\n{valor}! = 1')
    elif (valor < 0):
        print('\nNão existe Fatorial para o número informado...')
    else:
        fatorial = valor
        while (valor > 1):
            valor -= 1
            fatorial *= valor
    print(f'\n{valor_informado}! = {fatorial}')