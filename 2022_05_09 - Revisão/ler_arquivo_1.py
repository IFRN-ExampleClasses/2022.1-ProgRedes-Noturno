import os, sys

os.system('cls')

# Obtendo o diretório corrente
diretorio_atual = os.path.realpath(__file__)
diretorio_atual = os.path.dirname(diretorio_atual)

nome_arquivo = diretorio_atual + '\\servidores.csv'
arquivo_log  = diretorio_atual + '\\log_erro.txt'

try:
    print('-'*100)
    print('Abrindo o arquivo: {0}'.format(nome_arquivo))
    arquivo_input = open(nome_arquivo, 'r', encoding='utf-8')
    arquivo_log_input = open(arquivo_log, 'w', encoding='utf-8')
except FileNotFoundError:
    print('\nDeu ERRO...\nArquivo NÃO EXISTE...')
except PermissionError:
    print('\nDeu ERRO...\nArquivo JÁ ABERTO...')
except:
    print('\nDeu ERRO...', sys.exc_info()[0])
else:
    # Lendo os dados do arquivo de input e adicionando em uma lista
    print('\nLendo os dados do arquivo...\n')
    dados_input = list()
    # Ler a primeira linha do arquivo (titulos de cada campo)
    linha = arquivo_input.readline()
    while True:
        linha = arquivo_input.readline()[:-1]
        if linha == '': break
        try:
            dados_input.append(linha.split(';'))
        except:
            arquivo_log_input.write(linha)
    # Fechar o arquivo
    arquivo_input.close()
    arquivo_log_input.close()

    # Imprimindo a lista DADOS_INPUT uma posição por vez
    for i in dados_input: 
        print(i)
        print('')
        break
finally:
    print('\nPrograma Encerrado...\n')
