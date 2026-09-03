# Importando bibliotecas:
import os # Para limpar o terminal
import random # Para gerar uma matriz aleatória
import time # Para criar intervalos de tempo entre as gerações

# Adicionando variáveis globais para uso posterior:
tamanho = 10 # Número de linhas e colunas da matriz (para gerar uma matriz 10 por 10)
viva = 'O' # Representa as células vivas
morta = '.' # Representa as células mortas

def matriz_aleatoria():
    return [[random.choice([viva, morta]) for i in range(tamanho)] for j in range(tamanho)] # Gera uma matriz aleatória com
                                                                                            # células vivas e mortas

def exibir_matriz(matriz):
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa o terminal

    for linha in matriz:
        print(' '.join(linha)) # Separa cada célula por um espaço vazio

def matriz_personalizada():
    matriz = [[morta for i in range(tamanho)] for j in range(tamanho)] # Inicializa a matriz com células mortas

    print('Para personalizar a matriz você deve informar as linhas e as colunas (de 1 a 10, da esquerda para a direita) das ' \
          'células que deseja inicializar vivas: ')
    
    while True:
        try:
            linha = int(input('Em qual linha você deseja inserir uma célula viva?\n')) # O usuário deve informar em qual linha
                                                                                       # ele deseja adicionar uma célula viva

            if 1 <= linha <= tamanho: # Verifica se a linha informada pelo usuário está dentro do padrão aceitável (1 a 10)
                linha -= 1 # Ajusta para os padrões de uma lista/matriz
            else:
                print('Linha inválida, tente novamente.')

                continue

            coluna = int(input('Agora informe a coluna: ')) # Após informar a linha, o usuário deve informar a coluna que deseja
                                                            # adicionar uma célula viva

            if 1 <= coluna <= tamanho: # Verifica se a coluna informada pelo usuário está dentro do padrão aceitável (1 a 10)
                coluna -= 1 # Ajusta para os padrões de uma lista/matriz

                # Verifica se a célula já foi informada pelo usuário:
                if matriz[linha][coluna] == viva:
                    print('Você já informou que esta célula está viva, informe outra.')

                    continue
                else:
                    matriz[linha][coluna] = viva # Adiciona uma célula viva na linha e coluna informadas pelo usuário
            else:
                print('Coluna inválida, tente novamente.')

                continue

            while True:
                opcao_matriz = input('Deseja adicionar mais células vivas? Tecle "s" para sim ou "n" para não: ').strip().upper()

                if opcao_matriz == 'S':
                    break
                elif opcao_matriz == 'N':
                    ver_matriz = input('Deseja visualizar a matriz gerada? Tecle "s" para sim ou "n" para não: ').strip().upper()

                    if ver_matriz == 'S':
                        exibir_matriz(matriz)

                        try:
                            continuar = int(input('Deseja adicionar mais células vivas ou iniciar o jogo? Tecle "1" para ' \
                                                  'iniciar o jogo ou "2" para adicionar mais células vivas: '))

                            if continuar == 1:
                                return matriz
                            elif continuar == 2:
                                break
                            else:
                                print('Opção inválida, tente novamente.')
                        except ValueError:
                            print('Valor inválido, tente novamente.')
                    elif ver_matriz == 'N':
                        input('Pressione qualquer tecla para iniciar o jogo: ')
                        return matriz
                    else:
                        print('Opção inválida, tente novamente.')
                else:
                    print('Opção inválida, tente novamente.')
        except ValueError:
            print('Valor inválido, tente novamente.')

def contar_vizinhos(matriz, x, y):
    vivos = 0
    # Verifica os vizinhos
    vizinhos = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Percorre os vizinhos
    for dx, dy in vizinhos:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < tamanho and 0 <= ny < tamanho: # Verifica se está dentro dos limites da matriz
            if matriz[nx][ny] == viva:
                vivos += 1

    return vivos

def matrizes_iguais(matriz_1, matriz_2):
    return matriz_1 == matriz_2 # Verifica se a matriz atual é igual à anterior

def matriz_copia(matriz):
    return [linha[:] for linha in matriz] # Copia a matriz para adicioná-la no histórico e verificar se há padrão repetitivo

def proxima_geracao(matriz):
    matriz_nova = [[morta for i in range(tamanho)] for j in range(tamanho)]  # Gera uma matriz vazia
    
    for i in range(tamanho):
        for j in range(tamanho):
            vivos = contar_vizinhos(matriz, i, j)

            if matriz[i][j] == viva and vivos in [2, 3]:
                matriz_nova[i][j] = viva 
            elif matriz[i][j] == morta and vivos == 3:
                matriz_nova[i][j] = viva
    
    return matriz_nova

def jogo_da_vida():
    print('Jogo da vida:')
    print('Você deseja inicializar o jogo da vida com uma matriz aleatória ou uma matriz personalizada?')

    while True:
        geracao = 0
        historico = [] # Inicializa um histórico vazio para uso posterior

        try:
            opcao_jogo = int(input('Digite 1 para inicializar uma matriz aleatória ou 2 para inicializar uma matriz ' \
                                   'personalizada: '))

            if opcao_jogo == 1:
                matriz = matriz_aleatoria()

                break
            elif opcao_jogo == 2:
                matriz = matriz_personalizada()

                break
            else:
                print('Opção inválida, tente novamente.')
        except ValueError:
            print('Valor inválido, tente novamente.')

    exibir_matriz(matriz) # Exibe a matriz do jogo
    print(f'Geração: {geracao}') # Exibe a geração atual
    time.sleep(1) # Dá uma pausa de um segundo entre as gerações
    historico.append(matriz_copia(matriz))  # Salva a matriz inicial no histórico

    while True:
        matriz = proxima_geracao(matriz)
        geracao += 1

        exibir_matriz(matriz)
        print(f'Geração: {geracao}')

        time.sleep(1)

        # Percorre o histórico para identificar possível padrão repetitivo
        for antiga in historico:
            if matrizes_iguais(matriz, antiga):
                print(f'Vida parada na {geracao}ª geração.')

                return

        historico.append(matriz_copia(matriz)) # Salva a geração no histórico

# Chama a função principal
if __name__ == '__main__':
    jogo_da_vida()