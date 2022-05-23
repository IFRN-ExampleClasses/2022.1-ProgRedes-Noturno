raio = float(input('Informe o Raio: '))

if (raio > 0):
    pi = 3.14
    area = pi * raio * raio
    comprimento = 2 * pi * raio
    print('O Comprimento da Circunferência é', comprimento)
    print('A Área do Círculo é', area)
else:
    print('Informe um raio positivo...')