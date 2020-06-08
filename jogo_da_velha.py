import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("JOGO DA VELHA")
source_x = pygame.image.load("x.png").convert_alpha()
source_o = pygame.image.load("o.png").convert_alpha()
icon_o = pygame.transform.scale(source_o, (150, 150))
icon_x = pygame.transform.scale(source_x, (150, 150))
ganhador_x = pygame.transform.scale(source_x, (250, 250))
ganhador_o = pygame.transform.scale(source_o, (250, 250))
tabuleiro = [['?', '?', '?'],
             ['?', '?', '?'],
             ['?', '?', '?']]
step = 0

def jogador(step):
    if step % 2 == 0:
        jogador = 'X'
    else:
        jogador = '0'
    return jogador

def status(M):
    #verificando se jogador X ganhou na linha
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[i][j] == "X":
                #print(cont)
                cont+=1
        if cont == 3:
            return True

    #verificando se jogador 0 ganhou na linha
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[i][j] == "0":
                cont+=1
        if cont == 3:
            return True

    #verificando se jogador X ganhou na coluna
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[j][i] == "X":
                cont+=1
        if cont == 3:
            return True

    #verificando se jogador 0 ganhou na coluna
    for i in range(3):
        cont = 0
        for j in range(3):
            if M[j][i] == "0":
                cont+=1
        if cont == 3:
            return True

    #verificando se jogador X ganhou na diagonal principal
    cont = 0
    for i in range(3):        
        for j in range(3):
            if i == j:
                if M[j][i] == "X":
                    cont+=1
    if cont == 3:
        return True
        
    #verificando se jogador 0 ganhou na diagonal principal
    cont = 0
    for i in range(3):        
        for j in range(3):
            if i == j:
                if M[j][i] == "0":
                    cont+=1
    if cont == 3:
        return True


    #verificando se jogador X ganhou na diagonal secundária
    cont = 0
    for i in range(3):        
        for j in range(3):
            if i+j == 2:
                if M[j][i] == "X":
                    cont+=1
    if cont == 3:
        return True


    #verificando se jogador 0 ganhou na diagonal secundária
    cont = 0
    for i in range(3):        
        for j in range(3):
            if i+j == 2:
                if M[j][i] == "0":
                    cont+=1
    if cont == 3:
        return True

    #se ninguém venceu
    return False

def clickposition(x, y):
    if x < 195:
        x = (195-150)//2
    elif x < 395:
        x = 205 + (190-150)//2
    else:
        x = 405 + (195-150)//2
    if y < 195:
        y = (195-150)//2
    elif y < 395:
        y = 205 + (190-150)//2
    else:
        y = 405 + (195-150)//2
    return x, y

def blitar(jogador, posi_x, posi_y):
    screen.blit(jogador, (posi_x, posi_y))
    
def convert_position(x, y):
    if x == (195-150)//2:
        index_x = 0
    elif x == 205 + (190-150)//2:
        index_x = 1
    else:
        index_x = 2
    if y == (195-150)//2:
        index_y = 0
    elif y == 205 + (190-150)//2:
        index_y = 1
    else:
        index_y = 2
    return index_x, index_y

jogo = True
while True:
    
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    
    
    while jogo:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.draw.line(screen, (255, 255, 255), (195,0),(195, 600),10)
        pygame.draw.line(screen, (255, 255, 255), (395,0),(395, 600),10)
        pygame.draw.line(screen, (255, 255, 255), (0,195),(600, 195),10)
        pygame.draw.line(screen, (255, 255, 255), (0,395),(600, 395),10)
            
        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posi_x = event.pos[0]
            posi_y = event.pos[1]
            posi_x, posi_y = clickposition(posi_x, posi_y)
            index_x, index_y = convert_position(posi_x, posi_y)
            if tabuleiro[index_y][index_x] == "?":
                if step % 2 == 0:
                    blitar(icon_x, posi_x, posi_y)
                    tabuleiro[index_y][index_x] = 'X'
                else:
                    blitar(icon_o, posi_x, posi_y)
                    tabuleiro[index_y][index_x] = '0'
                pygame.display.flip()
                if status(tabuleiro):
                    jogador = jogador(step)
                    print('Parabens jogador {} voce ganhou o jogo'.format(jogador))
                    jogo = False
                step += 1
                if step == 9 and status(tabuleiro) == False:
                    jogador = 'empatou'
                    jogo = False
    pygame.time.delay(500)
    screen.fill((0, 0, 0))
    if jogador != 'empatou':
        if jogador == 'X':
            screen.blit(ganhador_x, (175, 120))
        elif jogador == '0':
            screen.blit(ganhador_o, (175, 120))
        font = pygame.font.Font(None, 50)
        text = font.render('Ganhou!', 1, (255, 255, 255))
        text_pos = text.get_rect(center = (300, 420))
        screen.blit(text, text_pos)
    else:
        font = pygame.font.Font(None, 50)
        text = font.render('Empatou!', 1, (255, 255, 255))
        text_pos = text.get_rect(center = (300, 340))
        screen.blit(text, text_pos)
    pygame.display.flip()

            
            

pygame.quit()
sys.exit()
