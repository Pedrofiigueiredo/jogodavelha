# Criando a matriz 3x3
def initialize():
    tabuleiro = [ ['a','a','a'], ['a','a','a'], ['a','a','a'] ]
    return tabuleiro

# Imprime o tabuleiro formatado no terminal
def Print(M):
    print('''  
 {0} ¦ {1} ¦ {2}
———¦———¦———
 {3} ¦ {4} ¦ {5}
———¦———¦———
 {6} ¦ {7} ¦ {8}'''.format(M[0][0], M[0][1], M[0][2], M[1][0], M[1][1], M[1][2], M[2][0], M[2][1], M[2][2]))

# Função para fazer a jogada
def step(M, lin, col, gamer):

    if M[lin][col] == 'a':
        M[lin][col] = gamer
        return M
    elif M[lin][col] == 'X' or M[lin][col] == 'O':
        return False

# Ver o vencedor
def status(M):

    # Verificar todas as linhas
    for l in range(3):
        if M[l][0] == M[l][1] == M[l][2] != 'a':
            return True
    # Verificar todas as colunas
    for c in range(3):
        if M[0][c] == M[1][c] == M[2][c] != 'a':
            return True
    # Verificar as diagonais
    if M[0][0] == M[1][1] == M[2][2] != 'a':
        return True

    return False

def main():
    # Cria e imprime a matriz
    tabuleiro = initialize()
    Print(tabuleiro)
    print()

    # Controla as jogadas
    rodada = 0
    while rodada != 9:
        # Jogada do X
        if rodada % 2 == 0:
            print('-- Vez do X --')
            print()

            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            gamer = 'X'
            # Faz a jogada acontecer
            if step(tabuleiro, linha, coluna, gamer) == False: # Jogada inválida
                print('Essa posição já está ocupada. Tente em outra...')
                print()
                continue
            else: # Jogada válida
                Print(tabuleiro)
                print()
                rodada +=1 # Próximo jogador

        # Jogada do O
        else:
            print('-- Vez do O --')
            print()

            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            gamer = 'O'
            # Faz a jogada acontecer
            if step(tabuleiro, linha, coluna, gamer) == False: # Jogada inválida
                print('Essa posição já está ocupada. Tente em outra...')
                print()
                continue
            else: # Jogada válida
                Print(tabuleiro)
                print()
                rodada +=1 # Próximo jogador

        # Mostrar vencedor
        if status(tabuleiro) == True and rodada % 2 == 0:
            print('O é vencedor')
            break
        if status(tabuleiro) == True and rodada % 2 != 0:
            print('X é vencedor')
            break

main()
