import threading, time

def carro_f1(nome_piloto, velocidade_carro):
    global vencedor
    voltas = 0
    while voltas <= 5:
        time.sleep(1/velocidade_carro)
        voltas += 1
        print('PILOTO: {0}: {1} ....... VOLTA {2}'.format(nome_piloto, time.ctime(), voltas))
    print('{0} CONCLUIU A PROVA!!!'.format(nome_piloto))
    if vencedor == None: vencedor = nome_piloto

try:
    vencedor = None
    piloto_1 = threading.Thread(target=carro_f1, args=['Lewis Hamilton', 5], name='p1')
    piloto_2 = threading.Thread(target=carro_f1, args=['Sebastian Vettel', 2], name='p2')
    piloto_3 = threading.Thread(target=carro_f1, args=['Max Verstappen', 3], name='p3')

    piloto_1.start()
    piloto_2.start()
    piloto_3.start()

    piloto_1.join()
    piloto_2.join()
    piloto_3.join()

    print('\n\nO PILOTO {0} VENCEU A PROVA!!!!!\n\n'.format(vencedor))
except:
    print('ERRO: A corrida não pode ser iniciada...')