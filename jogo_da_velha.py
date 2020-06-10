# Bibliotecas
import pygame
import sys

# ----- SETUP -----

# Pygame settings
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("JOGO DA VELHA")

# Assets (images & fonts)
source_x = pygame.image.load("assets/x.png").convert_alpha()
source_o = pygame.image.load("assets/o.png").convert_alpha()

icon_o = pygame.transform.scale(source_o, (150, 150))
icon_x = pygame.transform.scale(source_x, (150, 150))

ganhador_x = pygame.transform.scale(source_x, (250, 250))
ganhador_o = pygame.transform.scale(source_o, (250, 250))

font = pygame.font.Font('assets/arial.ttf', 25)
medium_font = pygame.font.Font('assets/arial.ttf', 20)
small_font = pygame.font.Font('assets/arial.ttf', 17)


# ----- 'BACK-END' -----

tabuleiro = [['?', '?', '?'],
             ['?', '?', '?'],
             ['?', '?', '?']]
step = 0


# Define qual jogador tem a vez na rodada
def jogador(step):
    if step % 2 == 1:
        jogador = 'X'
    else:
        jogador = '0'
    return jogador


# Verifica vnecedor / empate
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


# ----- 'FRONT-END' -----

programa = True
menu = True
nome_x = False
nome_o = False
jogo = False
rank = False

while programa:

    # --- MENU / TELA INICIAL ---
    while menu:
        event = pygame.event.poll()

        # Sair do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Configurando textos ---  

        # Escrever texto
        text_game_title = medium_font.render('Jogo da Velha', 0, (255, 255, 255))
        text_ranking = font.render('Ranking de jogadores', 0, (255, 255, 255))
        text_start = font.render('Jogar', 0, (255, 255, 255))

        # Caixa por volta de 'Jogar'
        pygame.draw.rect(screen, (255, 0, 0), [240, 420, 120, 40])

        # Configurando posicionamento
        text_game_title_pos = text_game_title.get_rect(center = (300, 260))
        text_ranking_pos = text_ranking.get_rect(center = (300, 390))
        text_start_pos = text_start.get_rect(center = (300, 440))

        # Imprime os textos
        screen.blit(text_game_title, text_game_title_pos)
        screen.blit(text_ranking, text_ranking_pos)
        screen.blit(text_start, text_start_pos)

        # Ícone do jogo da velha na parte superior
        pygame.draw.line(screen, (255, 255, 255), (275,80),(275, 230),5)
        pygame.draw.line(screen, (255, 255, 255), (325,80),(325, 230),5)
        pygame.draw.line(screen, (255, 255, 255), (225,130),(375, 130),5)
        pygame.draw.line(screen, (255, 255, 255), (225,180),(375, 180),5)
        pygame.display.flip()

        # Configurando os botões clicáveis
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 262 < x < 341 and 357 < y < 384:
                rank = True
                menu = False
            elif 262 < x < 338 and 428 < y < 452:
                nome_x = True
                menu = False


    # ----- INSERIR NOME DOS JOGADORES -----

    x_player_name = ''
    o_player_name = ''
    
    while nome_x:
        
        for event in pygame.event.get():
            # Sair do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    x_player_name = x_player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    nome_x = False
                    nome_o = True
                else:
                    x_player_name += event.unicode
        
        screen.fill((80,80,80))

        # Fundo
        pygame.draw.line(screen, (200, 200, 200), (195,0),(195, 600),10)
        pygame.draw.line(screen, (200, 200, 200), (395,0),(395, 600),10)
        pygame.draw.line(screen, (200, 200, 200), (0,195),(600, 195),10)
        pygame.draw.line(screen, (200, 200, 200), (0,395),(600, 395),10)

        #pos inicial X, pos inicial Y, largura, altura
        pygame.draw.rect(screen, (0, 0, 0), [120, 220, 365, 160])
        input_rect = pygame.Rect(170, 290, 270, 40)

        # Escrever textos
        title = small_font.render('Nome do jogador X', 0, (255, 255, 255))

        # Configurando posicionamento
        title_pos = title.get_rect(center = (300, 250))

        pygame.draw.rect(screen, (255, 39, 53), input_rect, 3)
        text_surface = small_font.render(x_player_name, True, (255, 255, 255))

        # Imprimir os textos
        screen.blit(text_surface, (180, 300))
        screen.blit(title, title_pos)

        pygame.display.flip()
    
    while nome_o:
        
        for event in pygame.event.get():
            # Sair do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    o_player_name = o_player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    nome_o = False
                    jogo = True
                else:
                    o_player_name += event.unicode
        
        screen.fill((80,80,80))

        # Fundo
        pygame.draw.line(screen, (200, 200, 200), (195,0),(195, 600),10)
        pygame.draw.line(screen, (200, 200, 200), (395,0),(395, 600),10)
        pygame.draw.line(screen, (200, 200, 200), (0,195),(600, 195),10)
        pygame.draw.line(screen, (200, 200, 200), (0,395),(600, 395),10)

        #pos inicial X, pos inicial Y, largura, altura
        pygame.draw.rect(screen, (0, 0, 0), [120, 220, 365, 160])
        input_rect = pygame.Rect(170, 290, 270, 40)

        # Escrever textos
        title = small_font.render('Nome do jogador O', 0, (255, 255, 255))

        # Configurando posicionamento
        title_pos = title.get_rect(center = (300, 250))

        pygame.draw.rect(screen, (255, 39, 53), input_rect, 3)
        text_surface = small_font.render(o_player_name, True, (255, 255, 255))

        # Imprimir os textos
        screen.blit(text_surface, (180, 300))
        screen.blit(title, title_pos)

        pygame.display.flip()

    # ----- 'PÁGINA' DO RANKING DE JOGADORES -----
    while rank:
        pass
    
    screen.fill((0, 0, 0))

    # ----- JOGO -----
    while jogo:
        while step < 9:
            
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
                    step += 1
                    if step % 2 == 1:
                        blitar(icon_x, posi_x, posi_y)
                        tabuleiro[index_y][index_x] = 'X'
                    else:
                        blitar(icon_o, posi_x, posi_y)
                        tabuleiro[index_y][index_x] = '0'
                    pygame.display.flip()
                    
                    if status(tabuleiro):
                        jogador = jogador(step)
                        print('Parabens jogador {} voce ganhou o jogo'.format(jogador))
                        break
                    if step == 9 and status(tabuleiro) == False:
                        jogador = 'empatou'
                        break
                        
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

        jogo = False
    
    # TELA FINAL (jogar de novo, ver ranking ou sair do jogo)
        
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()
sys.exit()