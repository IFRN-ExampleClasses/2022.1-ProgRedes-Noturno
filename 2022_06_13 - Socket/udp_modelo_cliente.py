# Importando a biblioteca socket
import socket

HOST = 'localhost'  #Definindo o IP do servidor
PORT = 50000        #Definindo a porta
CODE_PAGE = 'utf-8' # Definindo a página de codificação de caracteres

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitando a mensagem
    msg = input('Digite a mensagem (EXIT p/ sair): ')
    if msg.upper() == 'EXIT': break
    # Convertendo a mensagem digitada de string para bytes
    msg = msg.encode(CODE_PAGE)
    # Enviando a mensagem ao servidor      
    udp_socket.sendto(msg, (HOST, PORT))

# Fechando o socket
udp_socket.close()
