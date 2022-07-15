import threading, time, random

def carro_f1(nome_piloto):
    global vencedor
    voltas = 0
    while voltas <= 5:
        velocidade_carro = random.randint(1,5)
        time.sleep(1/velocidade_carro)
        voltas += 1
        print('PILOTO: {0}: {1} ....... VOLTA {2}'.format(nome_piloto, time.ctime(), voltas))
    print('{0} CONCLUIU A PROVA!!!'.format(nome_piloto))
    if vencedor == None: vencedor = nome_piloto

try:
    vencedor = None
    piloto_1 = threading.Thread(target=carro_f1, args=['Lewis Hamilton'], name='p1')
    piloto_2 = threading.Thread(target=carro_f1, args=['Sebastian Vettel'], name='p2')
    piloto_3 = threading.Thread(target=carro_f1, args=['Max Verstappen'], name='p3')

    piloto_1.start()
    piloto_2.start()
    piloto_3.start()

    piloto_1.join()
    piloto_2.join()
    piloto_3.join()

    print('\n\nO PILOTO {0} VENCEU A PROVA!!!!!\n\n'.format(vencedor))
except:
    print('ERRO: A corrida não pode ser iniciada...')