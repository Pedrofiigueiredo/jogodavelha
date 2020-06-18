# Bibliotecas
import pygame
import sys

# Arquivos da modularização
import game
from game import tabuleiro
from game import step

# ----- SETUP -----

# Pygame settings
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("JOGO DA VELHA")

# Assets (images & fonts)
source_x = pygame.image.load("assets/x.png").convert_alpha()
source_o = pygame.image.load("assets/o.png").convert_alpha()

icone = pygame.image.load('assets/icone.png').convert_alpha()
icone2 = pygame.image.load('assets/icone2.png').convert_alpha()
sound = pygame.image.load('assets/sound.png').convert_alpha()
mute = pygame.image.load('assets/mute.png').convert_alpha()
trofeu = pygame.image.load('assets/trofeu.png').convert_alpha()
trofeu2 = pygame.image.load('assets/trofeu2.png').convert_alpha()
lstars = pygame.image.load('assets/lstars.png').convert_alpha()
rstars = pygame.image.load('assets/rstars.png').convert_alpha()
lstars2 = pygame.image.load('assets/lstars2.png').convert_alpha()
rstars2 = pygame.image.load('assets/rstars2.png').convert_alpha()

icon_o = pygame.transform.scale(source_o, (150, 150))
icon_x = pygame.transform.scale(source_x, (150, 150))

ganhador_x = pygame.transform.scale(source_x, (172, 172))
ganhador_o = pygame.transform.scale(source_o, (184, 184))

font = pygame.font.Font('assets/Pixellari.ttf', 25)
medium_font = pygame.font.Font('assets/Pixellari.ttf', 20)
small_font = pygame.font.Font('assets/Pixellari.ttf', 17)

font2 = pygame.font.Font('assets/fredokaone.ttf', 30)
medium_font2 = pygame.font.Font('assets/fredokaone.ttf', 17)
small_font2 = pygame.font.Font('assets/fredokaone.ttf', 14)

def blitar(jogador, posi_x, posi_y):
    screen.blit(jogador, (posi_x, posi_y))


# ----- CONFIGURAÇÕES PARA O RANKING DE JOGADORES -----

# Atualizar
def add_ranking(ganhador):

    arquivo = open('data/ranking.txt', 'r', encoding = 'utf8')
    count = 0

    gamer_names = []
    gamer_points = []

    # Adiciona os dados do ranking em vetores
    for lines in arquivo:
        lines = lines.rstrip()
        gamer_info = lines.split(':')
        gamer_names.append(gamer_info[0])
        gamer_points.append(int(gamer_info[1]))

    arquivo.close()

    # Tamanho do vetor
    gamer_qtd = len(gamer_names)

    for i in range(gamer_qtd):
        # Se o jogador já estiver 'cadastrado'
        if gamer_names[i] == ganhador:
            gamer_points[i] += 1
            arquivo.close()

            arquivo2 = open('data/ranking.txt', 'w', encoding = 'utf8')

            # Atualiza o número de pontos do jogador
            for i in range(gamer_qtd):
                arquivo2.write(gamer_names[i] + ':' + str(gamer_points[i]) + '\n')
            arquivo2.close()
            break

        count += 1

    # Se o jogador é novo (não tem nome no ranking)
    if count == gamer_qtd:
        arquivo3 = open('data/ranking.txt', 'a', encoding = 'utf8')
        arquivo3.write(ganhador + ':' +  '1' + '\n')
        arquivo3.close()
# Ordenar
def ordenar_ranking():
    arquivo = open('data/ranking.txt', 'r+', encoding = 'utf8')
    ranking = {}
    ordenado = []

    # Adiciona as informações do ranking em um dicionário
    for lines in arquivo:
        lines = lines.rstrip()
        gamer_info = lines.split(':')
        ranking[gamer_info[0]] = int(gamer_info[1])

    # Ordena o dicionário
    for item in sorted(ranking, key = ranking.get, reverse = True):
        ordenado.append('{}:{}'.format(item, ranking[item]))

    arquivo2 = open('data/ranking.txt', 'w', encoding = 'utf8')

    # Atualiza o arquivo ranking.txt com os dados ordenados
    for i in ordenado:
        arquivo2.write(i + '\n')

    arquivo2.close()
    arquivo.close()


# ----- INTERFACE -----

programa = True
menu = True
nome_x = False
nome_o = False
ranking = False
jogo = False

# ----------------------------------

while programa:

    # --- MENU / TELA INICIAL ---
    while menu:
        event = pygame.event.poll()

        # Sair do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # --- Configurando textos ---  

        font2 = pygame.font.Font('assets/fredokaone.ttf', 25)

        # Escrever texto
        text_game_title = font.render('JOGO DA VELHA', 0, (255, 255, 255))
        text_ranking = medium_font.render('Ranking de jogadores', 0, (255, 255, 255))
        text_start = font2.render('Jogar', 0, (255, 255, 255))

        # Caixa por volta de 'Jogar' | x, y, w, h
        pygame.draw.rect(screen, (255, 255, 255), [240, 280, 126, 46]) # Borda
        pygame.draw.rect(screen, (26, 99, 240), [243, 283, 120, 40])

        # Configurando posicionamento | center = (x, y)
        text_game_title_pos = text_game_title.get_rect(center=(300, 192))
        text_ranking_pos = text_ranking.get_rect(center=(310, 370))
        text_start_pos = text_start.get_rect(center=(303, 303))

        # Imprime os textos
        screen.blit(text_game_title, text_game_title_pos)
        screen.blit(text_ranking, text_ranking_pos)
        screen.blit(text_start, text_start_pos)

        # Imagens
        screen.blit(icone, (264, 87)) # Ícone do topo
        screen.blit(lstars, (145, 181)) # Estrelas da esquerda
        screen.blit(rstars, (418, 181)) # Estrelas da direita
        screen.blit(trofeu, (185, 358)) # Trofeu ao lado do ranking
        screen.blit(sound, (41, 521)) # Botão de som ativado
        screen.blit(icone2, (517, 510)) # Icone de baixo


        pygame.display.flip()

        # Configurando os botões clicáveis
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Ao clicar para ver o ranking
            if 262 < x < 341 and 357 < y < 384:
                ranking = True
                menu = False
            # Ao clicar para jogar | width = 120, height = 40
            elif 240 < x < 360 and 280 < y < 320:
                nome_x = True
                menu = False


    # ----- INSERIR NOME DOS JOGADORES -----
    x_player_name = ''
    o_player_name = ''

    while nome_x:
        # --- Inserir nome do jogador ---
        for event in pygame.event.get():

            # Sair do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Quando o usuário digitar no teclado...
            if event.type == pygame.KEYDOWN:
                # Habilita a tecla backspace (apagar caracter)
                if event.key == pygame.K_BACKSPACE:
                    x_player_name = x_player_name[:-1]

                # Habilita tecla enter (para prosseguir)
                elif event.key == pygame.K_RETURN:
                    x_name = x_player_name
                    print(x_name)

                    nome_x = False
                    nome_o = True
                
                # Habilita o usuário digitar o nome
                else:
                    x_player_name += event.unicode

        # --- Configurações da interface ---
        screen.fill((0,0,0))

        # Fundo
        pygame.draw.line(screen, (76, 76, 76), (195, 0), (195, 600), 10)
        pygame.draw.line(screen, (76, 76, 76), (395, 0), (395, 600), 10)
        pygame.draw.line(screen, (76, 76, 76), (0, 195), (600, 195), 10)
        pygame.draw.line(screen, (76, 76, 76), (0, 395), (600, 395), 10)

        # pos inicial X, pos inicial Y, largura, altura
        pygame.draw.rect(screen, (255, 255, 255), [90, 212, 426, 168]) # Borda
        pygame.draw.rect(screen, (26, 99, 240), [93, 215, 420, 162])
        input_rect = pygame.Rect(132, 281, 336, 45)

        # Escrever textos
        title = medium_font2.render('Nome do jogador X', 0, (255, 255, 255))
        description = medium_font2.render('Tecle ENTER para prosseguir', 0, (255, 255, 255))
        text_surface = small_font.render(x_player_name, True, (255, 255, 255))

        # Borda para o nome do usuário (caixa)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        # Configurando posicionamento
        title_pos = title.get_rect(center=(300, 250))
        description_pos = description.get_rect(center=(300, 350))

        # Imprimir os textos
        screen.blit(text_surface, (145, 296))
        screen.blit(title, title_pos)
        screen.blit(description, description_pos)

        # Imagens
        screen.blit(lstars2, (178, 240)) # Estrelas da esquerda
        screen.blit(rstars2, (385, 240)) # Estrelas da direita

        pygame.display.flip()

    while nome_o:
        # --- Inserir nome do jogador ---
        for event in pygame.event.get():

            # Sair do jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Quando o usuário digitar no teclado...
            if event.type == pygame.KEYDOWN:
                # Habilita a tecla backspace (apagar caracter)
                if event.key == pygame.K_BACKSPACE:
                    o_player_name = o_player_name[:-1]

                # Habilita tecla enter (para prosseguir)
                elif event.key == pygame.K_RETURN:
                    o_name = o_player_name
                    print(o_name)
                    
                    nome_o = False
                    jogo = True
                
                # Habilita o usuário digitar o nome
                else:
                    o_player_name += event.unicode

        # --- Configurações da interface ---
        screen.fill((0,0,0))

        # Fundo
        pygame.draw.line(screen, (76, 76, 76), (195, 0), (195, 600), 10)
        pygame.draw.line(screen, (76, 76, 76), (395, 0), (395, 600), 10)
        pygame.draw.line(screen, (76, 76, 76), (0, 195), (600, 195), 10)
        pygame.draw.line(screen, (76, 76, 76), (0, 395), (600, 395), 10)

        # pos inicial X, pos inicial Y, largura, altura
        pygame.draw.rect(screen, (255, 255, 255), [90, 212, 426, 168]) # Borda
        pygame.draw.rect(screen, (26, 99, 240), [93, 215, 420, 162])
        input_rect = pygame.Rect(132, 281, 336, 45)

        # Escrever textos
        title = medium_font2.render('Nome do jogador O', 0, (255, 255, 255))
        description = small_font.render('Tecle ENTER para prosseguir', 0, (255, 255, 255))
        text_surface = medium_font2.render(o_player_name, True, (255, 255, 255))

        # Borda para o nome do usuário (caixa)
        pygame.draw.rect(screen, (255, 255, 255), input_rect, 3)

        # Configurando posicionamento
        title_pos = title.get_rect(center=(300, 250))
        description_pos = description.get_rect(center=(300, 350))

        # Imprimir os textos
        screen.blit(text_surface, (145, 293))
        screen.blit(title, title_pos)
        screen.blit(description, description_pos)

        # Imagens
        screen.blit(lstars2, (178, 240)) # Estrelas da esquerda
        screen.blit(rstars2, (385, 240)) # Estrelas da direita

        pygame.display.flip()


    # ----- 'PÁGINA' DO RANKING DE JOGADORES -----
    while ranking:

        event = pygame.event.poll()

        # Sair do jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.fill((0, 0, 0))

        # --- Configurando textos estáticos ---  

        font2 = pygame.font.Font('assets/fredokaone.ttf', 25)

        # Escrever texto
        text_title = font.render('Ranking de Jogadores', 0, (255, 255, 255))
        text_description = small_font2.render('Top 5 jogadores', 0, (255, 255, 255))
        text_player_name = medium_font2.render('Nome do jogador', 0, (255, 255, 255))
        text_points = medium_font2.render('Número de vitórias', 0, (255, 255, 255))
        text_start = font2.render('Jogar', 0, (255, 255, 255))

        # [Botão] Caixa por volta de 'Jogar' | x, y, w, h
        pygame.draw.rect(screen, (255, 255, 255), [388, 521, 169, 46]) # Borda
        pygame.draw.rect(screen, (26, 99, 240), [391, 524, 163, 40])

        # Configurando posicionamento | center = (x, y)
        text_title_pos = text_title.get_rect(center=(300, 110))
        text_description_pos = text_description.get_rect(center = (300, 140))

        # Imprime os textos
        screen.blit(text_title, text_title_pos) # Título (Ranking de Jogadores)
        screen.blit(text_description, text_description_pos) # 'Top 5 jogadores'
        screen.blit(text_player_name, (90, 171)) # 'Nome do Jogador'
        screen.blit(text_points, (355, 171)) # 'Número de Vitórias'
        screen.blit(text_start, (438, 528)) # Texto do botão Jogar

        # Imagens
        screen.blit(trofeu2, (279, 37)) # Ícone do topo
        screen.blit(lstars, (122, 100)) # Estrelas da esquerda
        screen.blit(rstars, (444, 100)) # Estrelas da direita
        screen.blit(sound, (41, 521)) # Botão de som ativado


        # --- Configuração dos nomes e pontos dos jogadores ---

        arquivo = open('data/ranking.txt', 'r')

        top5_names = []
        top5_points = []

        c = 0
        for lines in arquivo:
            lines = lines.rstrip()
            gamer_info = lines.split(':')
            top5_names.append(gamer_info[0])
            top5_points.append(gamer_info[1])

            c += 1

            if c == 5:
                break


        # Escrever textos
        player_name_1 = small_font2.render(top5_names[0], 0, (255, 255, 255))
        player_name_2 = small_font2.render(top5_names[1], 0, (255, 255, 255))
        player_name_3 = small_font2.render(top5_names[2], 0, (255, 255, 255))
        player_name_4 = small_font2.render(top5_names[3], 0, (255, 255, 255))
        player_name_5 = small_font2.render(top5_names[4], 0, (255, 255, 255))

        pedro = small_font2.render('Pedro Figueiredo Dias', 0, (255, 255, 255))
        lucas = small_font2.render('Ye Wei Jiang', 0, (255, 255, 255))
        claudio = small_font2.render('Claudio Siqueira Ramos Junior', 0, (255, 255, 255))

        points_1 = small_font2.render(top5_points[0], 0, (255, 255, 255))
        points_2 = small_font2.render(top5_points[1], 0, (255, 255, 255))
        points_3 = small_font2.render(top5_points[2], 0, (255, 255, 255))
        points_4 = small_font2.render(top5_points[3], 0, (255, 255, 255))
        points_5 = small_font2.render(top5_points[4], 0, (255, 255, 255))

        tia_pedro = small_font2.render('4199045-5', 0, (255, 255, 255))
        tia_lucas = small_font2.render('4192629-3', 0, (255, 255, 255))
        tia_claudio = small_font2.render('4191656-5', 0, (255, 255, 255))

        # Configuração de posicionamento
        points_1_pos = points_1.get_rect(center = (428, 225))
        points_2_pos = points_2.get_rect(center = (428, 250))
        points_3_pos = points_3.get_rect(center = (428, 275))
        points_4_pos = points_4.get_rect(center = (428, 300))
        points_5_pos = points_5.get_rect(center = (428, 325))

        tia_pedro_pos = tia_pedro.get_rect(center = (428, 385))
        tia_lucas_pos = tia_lucas.get_rect(center = (428, 410))
        tia_claudio_pos = tia_claudio.get_rect(center = (428, 435))

        # Imprime os textos
        screen.blit(player_name_1, (90, 215))
        screen.blit(player_name_2, (90, 240))
        screen.blit(player_name_3, (90, 265))
        screen.blit(player_name_4, (90, 290))
        screen.blit(player_name_5, (90, 315))

        screen.blit(pedro, (90, 370))
        screen.blit(lucas, (90, 395))
        screen.blit(claudio, (90, 420))

        screen.blit(points_1, points_1_pos)
        screen.blit(points_2, points_2_pos)
        screen.blit(points_3, points_3_pos)
        screen.blit(points_4, points_4_pos)
        screen.blit(points_5, points_5_pos)

        screen.blit(tia_pedro, tia_pedro_pos)
        screen.blit(tia_lucas, tia_lucas_pos)
        screen.blit(tia_claudio, tia_claudio_pos)

        pygame.display.flip()
        arquivo.close()

        # Configurando os botões clicáveis
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Ao clicar no botão jogar
            if 388 < x < 557 and 521 < y < 567:
                nome_x = True
                ranking = False
        

    # ----- JOGO -----
    continua = True
    tela_final = True

    while jogo:
        screen.fill((0, 0, 0))

        # Enquanto o jogo não acabou
        while continua:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Tabuleiro do jogo (#)
            pygame.draw.line(screen, (255, 255, 255), (195, 0), (195, 600), 10)
            pygame.draw.line(screen, (255, 255, 255), (395, 0), (395, 600), 10)
            pygame.draw.line(screen, (255, 255, 255), (0, 195), (600, 195), 10)
            pygame.draw.line(screen, (255, 255, 255), (0, 395), (600, 395), 10)

            pygame.display.flip()

            # Receber jogadas
            if event.type == pygame.MOUSEBUTTONDOWN:
                posi_x = event.pos[0]
                posi_y = event.pos[1]
                posi_x, posi_y = game.clickposition(posi_x, posi_y)
                index_x, index_y = game.convert_position(posi_x, posi_y)

                # Se a posição for válida...
                if tabuleiro[index_y][index_x] == "?":
                    step += 1

                    # Vez do jogador X
                    if step % 2 == 1:
                        blitar(icon_x, posi_x, posi_y)
                        tabuleiro[index_y][index_x] = 'X'

                    # Vez do jogador O
                    else:
                        blitar(icon_o, posi_x, posi_y)
                        tabuleiro[index_y][index_x] = '0'
                    pygame.display.flip()

                    # --- Quando acabar o jogo...---

                    # Vitória de um dos jogadores
                    if game.status(tabuleiro):
                        jogador = game.jogador(step)
                        print('Parabens jogador {} voce ganhou o jogo'.format(jogador))
                        
                        # --- Atualiza o ranking de jogadores com o vencedor ---
                        if jogador == 'X':
                            ganhador = x_name
                        else:
                            ganhador = o_name
                        
                        # Todos os nomes vão para o ranking com UPPER case
                        add_ranking(ganhador.upper())
                        ordenar_ranking()

                        continua = False

                    # Empate
                    if step == 9 and game.status(tabuleiro) == False:
                        jogador = 'empatou'
                        continua = False
                
                # Se a posição não for válida (já estiver ocupada), nada acontece


        # ----- TELA FINAL -----
        pygame.time.delay(500)
        screen.fill((0, 0, 0))

        # Algum dos jogadores ganhou...
        if jogador != 'empatou':
            if jogador == 'X':
                screen.blit(ganhador_x, (208, 45))
                vencedor = 'x'
            elif jogador == '0':
                screen.blit(ganhador_o, (208, 45))
                vencedor = 'o'
            
            # Configurações do texto
            text = font2.render('Ganhou!', 1, (255, 255, 255))
            text_pos = text.get_rect(center=(300, 250))
            screen.blit(text, text_pos)

            font = pygame.font.Font('assets/Pixellari.ttf', 27)
            parabens = font.render('Parabéns, {}!'.format(ganhador), 1, (255, 255, 255))
            parabens_pos = parabens.get_rect(center=(300, 290))
            screen.blit(parabens, parabens_pos)

        # Empate...
        else:
            text = font2.render('Empate!', 1, (255, 255, 255))
            text_pos = text.get_rect(center=(300, 200))
            screen.blit(text, text_pos)

            font = pygame.font.Font('assets/Pixellari.ttf', 27)
            description = font.render('Deu velha... Bora jogar de novo!', 1, (255, 255, 255))
            description_pos = description.get_rect(center=(300, 240))
            screen.blit(description, description_pos)

        # --- Opções (Ver ranking de jogadores, jogar de novo ou sair) ---

        # Escrever textos
        text_ranking = medium_font.render('Ranking de jogadores', 0, (255, 255, 255))
        text_restart = medium_font.render('Jogar de novo', 0, (255, 255, 255))
        text_quit = medium_font.render('Sair do jogo', 0, (255, 255, 255))

        # Escrever textos
        text_ranking_pos = text_ranking.get_rect(center=(310, 410))
        text_restart_pos = text_restart.get_rect(center=(300, 460))
        text_quit_pos = text_quit.get_rect(center=(300, 510))

        # --- Formas geométricas (botões) ---
        # Caixa por volta de 'Jogar' | x, y, w, h
        pygame.draw.rect(screen, (255, 255, 255), [178, 435, 250, 46]) # Borda
        pygame.draw.rect(screen, (26, 99, 240), [181, 438, 244, 40])

        # Imprimir os textos
        screen.blit(text_quit, text_quit_pos)
        screen.blit(text_restart, text_restart_pos)
        screen.blit(text_ranking, text_ranking_pos)

        screen.blit(trofeu, (185, 398)) # Trofeu ao lado do ranking

        pygame.display.flip()


        while tela_final:
            for event in pygame.event.get():

                # Sair do jogo (clicando no botão fora da janela)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Configurando botões clicáveis
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posi_x, posi_y = event.pos

                    if 183 <= posi_x <= 417:

                        # Ao clicar em ver ranking
                        if 387 <= posi_y <= 435:
                            ranking = True
                            jogo = False
                        # Ao clicar em jogar de novo...
                        elif 435 < posi_y <= 485:
                            step = 0
                            continua = True
                            tabuleiro = [['?', '?', '?'],
                                         ['?', '?', '?'],
                                         ['?', '?', '?']]
                            break
                        # Ao clicar em sair...
                        elif 485 < posi_y <= 533:
                            pygame.quit()
                            sys.exit()
            break

# ----------------------------------

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

pygame.quit()
sys.exit()
