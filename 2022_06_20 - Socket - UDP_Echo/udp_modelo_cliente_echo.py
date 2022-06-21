# Importando a biblioteca socket
import socket

HOST        = 'localhost' # Definindo o IP do servidor
PORT        = 40000       # Definindo a porta
CODE_PAGE   = 'utf-8'     # Definindo a página de codificação de caracteres
BUFFER_SIZE = 512         # Definindo o tamanho do buffer

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
    # Recebendo echo do servidor
    data_retorno, ip_retorno = udp_socket.recvfrom(4096)
    msg_retorno = data_retorno.decode(CODE_PAGE)
    print (f'Echo recebido {ip_retorno}: {msg_retorno} ')
# Fechando o socket
udp_socket.close()
