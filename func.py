# Define qual jogador tem a vez na rodada
def jogador(step):
    if step % 2 == 1:
        jogador = 'X'
    else:
        jogador = '0'
    return jogador


# Verifica vencedor / empate
def status(M):
    # verificando se jogador X ganhou na linha
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[i][j] == "X":
                # print(cont)
                cont += 1
        if cont == 3:
            return True

    # verificando se jogador 0 ganhou na linha
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[i][j] == "0":
                cont += 1
        if cont == 3:
            return True

    # verificando se jogador X ganhou na coluna
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[j][i] == "X":
                cont += 1
        if cont == 3:
            return True

    # verificando se jogador 0 ganhou na coluna
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[j][i] == "0":
                cont += 1
        if cont == 3:
            return True

    # verificando se jogador X ganhou na diagonal principal
    cont = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if M[j][i] == "X":
                    cont += 1
    if cont == 3:
        return True

    # verificando se jogador 0 ganhou na diagonal principal
    cont = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if M[j][i] == "0":
                    cont += 1
    if cont == 3:
        return True

    # verificando se jogador X ganhou na diagonal secundária
    cont = 0
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                if M[j][i] == "X":
                    cont += 1
    if cont == 3:
        return True

    # verificando se jogador 0 ganhou na diagonal secundária
    cont = 0
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                if M[j][i] == "0":
                    cont += 1
    if cont == 3:
        return True

    # se ninguém venceu
    return False


def clickposition(x, y):
    if x < 195:
        x = (195 - 150) // 2
    elif x < 395:
        x = 205 + (190 - 150) // 2
    else:
        x = 405 + (195 - 150) // 2
    if y < 195:
        y = (195 - 150) // 2
    elif y < 395:
        y = 205 + (190 - 150) // 2
    else:
        y = 405 + (195 - 150) // 2
    return x, y


def convert_position(x, y):
    if x == (195 - 150) // 2:
        index_x = 0
    elif x == 205 + (190 - 150) // 2:
        index_x = 1
    else:
        index_x = 2
    if y == (195 - 150) // 2:
        index_y = 0
    elif y == 205 + (190 - 150) // 2:
        index_y = 1
    else:
        index_y = 2
    return index_x, index_y
