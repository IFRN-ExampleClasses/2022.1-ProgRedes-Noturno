import time

def carro_f1(nome_piloto, velocidade_carro):
    voltas = 0
    while voltas <= 5:
        time.sleep(1/velocidade_carro)
        voltas += 1
        print('PILOTO: {0}: {1} ....... VOLTA {2}'.format(nome_piloto, time.ctime(), voltas))
    print('{0} CONCLUIU A PROVA!!!'.format(nome_piloto))

try:
    piloto_1 = carro_f1('Lewis Hamilton', 5)
    piloto_2 = carro_f1('Sebastian Vettel', 2)
    piloto_3 = carro_f1('Max Verstappen', 3)
except:
    print('ERRO: A corrida não pode ser iniciada...')