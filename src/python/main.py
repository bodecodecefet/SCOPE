import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configurações do botão
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 60
BUTTON_COLOR = (139, 69, 19)  # Marrom
BUTTON_BORDER_COLOR = (160, 82, 45)  # Marrom claro para borda
BUTTON_TEXT_COLOR = (0, 0, 0)  # Preto
BUTTON_TEXT_SIZE = 50

# Distância que os botões serão movidos para baixo (em pixels)
BUTTON_MOVE_DOWN1 = 30
BUTTON_MOVE_DOWN2 = 110

# Distância que os botões serão movidos para a direita (em pixels)
BUTTON_MOVE_RIGHT1 = 0
BUTTON_MOVE_RIGHT2 = 50

# Configurações do texto
TEXT_COLOR = (139, 69, 19)  # Marrom
TEXT_SIZE = 80

# Configurações do título do jogo
GAME_TITLE = "Scope: Mirando Certo"

# Lista de caminhos de imagem para as telas de pergunta
QUESTION_BACKGROUND_PATHS = [
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
    R"image\pergunta1.png",
]

# Criando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tela de Início")

# Carregando a imagem de fundo
background_image = pygame.image.load(R"image\fundo_menu.png").convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Função para criar o texto com bordas
def draw_text_with_borders(text, size, color, border_color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)

    # Ajuste este valor para aumentar ou diminuir o tamanho da borda
    border_offset = 5

    # Renderização da borda
    border_surface = font.render(text, True, border_color)
    border_rect = border_surface.get_rect(
        center=text_surface.get_rect(center=(x + border_offset, y + border_offset)).center)

    # Desenhar o texto na tela
    screen.blit(border_surface, border_rect)
    screen.blit(text_surface, text_surface.get_rect(center=(x, y)))

# Função para criar o botão na tela
def draw_button():
    button_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2 + BUTTON_MOVE_RIGHT1,  # Mover o botão para a direita
        SCREEN_HEIGHT - 180 + BUTTON_MOVE_DOWN1,  # Mover o botão para baixo
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
    )

    # Renderização do preenchimento do botão
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    # Renderização da borda do botão após o preenchimento
    button_border_surface = pygame.Surface((BUTTON_WIDTH + 6, BUTTON_HEIGHT + 6))
    button_border_surface.fill(BUTTON_BORDER_COLOR)
    button_border_rect = button_border_surface.get_rect(center=button_rect.center)
    screen.blit(button_border_surface, button_border_rect)

    button_text_surface = pygame.font.SysFont(None, BUTTON_TEXT_SIZE).render("Start", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text_surface.get_rect(center=button_rect.center)
    screen.blit(button_text_surface, button_text_rect)

# Variável de controle para determinar a página
current_page = "menu"

# Variável para armazenar a letra correspondente ao botão clicado
selected_letter = None

# Mapeamento de botões para letras
button_letter_mapping = {
    0: 'R',
    1: 'I',
    2: 'C',
    3: 'A',
    4: 'S',
    5: 'E',
}

# Contadores de cliques para cada botão
button_click_counts = {letter: 0 for letter in button_letter_mapping.values()}

# Função para mudar de página
def change_page(page):
    global current_page
    current_page = page

# Função para processar o clique do mouse nas telas de pergunta
def process_question_page_click(event):
    global selected_letter, current_question  # Tornar current_question global
    button_spacing = 55
    button_x_left = SCREEN_WIDTH // 4 - BUTTON_WIDTH // 20 + BUTTON_MOVE_RIGHT2  # Mover os botões para a direita
    button_x_right = 3 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2 + BUTTON_MOVE_RIGHT2  # Mover os botões para a direita
    button_y = SCREEN_HEIGHT // 4 - BUTTON_HEIGHT // 2 + BUTTON_MOVE_DOWN2  # Mover os botões para baixo

    for i in range(6):
        if i < 3:
            button_x = button_x_left
        else:
            button_x = button_x_right
        button_rect = pygame.Rect(
            button_x,
            button_y + (i % 3) * (BUTTON_HEIGHT + button_spacing),
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        if button_rect.collidepoint(event.pos):
            selected_letter = button_letter_mapping[i]
            # Atualiza o contador de cliques e exibe no terminal
            button_click_counts[selected_letter] += 1
            print(f"Botão {selected_letter} foi clicado durante a prova.")

            # Verifica se todas as perguntas foram respondidas
            if current_question == len(QUESTION_BACKGROUND_PATHS) - 1:
                print("Contagem de cliques:")
                for letter, count in button_click_counts.items():
                    print(f"Botão {letter} foi clicado {count} vezes no total.")
                pygame.quit()
                sys.exit()
            else:
                current_question += 1

# Variável de controle para determinar a pergunta atual
current_question = 0

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_page == "menu":
                button_rect = pygame.Rect(
                    SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2 + BUTTON_MOVE_RIGHT1,  # Mover o botão para a direita
                    SCREEN_HEIGHT - 180 + BUTTON_MOVE_DOWN1,  # Mover o botão para baixo
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                )
                if button_rect.collidepoint(event.pos):
                    current_question = 0
                    change_page("outra_pagina")
            elif current_page == "outra_pagina":
                process_question_page_click(event)

    screen.blit(background_image, (0, 0))

    if current_page == "menu":
        draw_text_with_borders(GAME_TITLE, TEXT_SIZE, TEXT_COLOR, (0, 0, 0), SCREEN_WIDTH // 2, 150)
        draw_button()
    elif current_page == "outra_pagina":
        if 0 <= current_question < len(QUESTION_BACKGROUND_PATHS):
            # Desenha a imagem de fundo da pergunta atual
            question_background_image = pygame.image.load(QUESTION_BACKGROUND_PATHS[current_question]).convert()
            question_background_image = pygame.transform.scale(question_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(question_background_image, (0, 0))

            # Desenha os botões na tela de pergunta
            # button_spacing = 55
            # button_x_left = SCREEN_WIDTH // 4 - BUTTON_WIDTH // 20 + BUTTON_MOVE_RIGHT2  # Mover os botões para a direita
            # button_x_right = 3 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2 + BUTTON_MOVE_RIGHT2  # Mover os botões para a direita
            # button_y = SCREEN_HEIGHT // 4 - BUTTON_HEIGHT // 2 + BUTTON_MOVE_DOWN2  # Mover os botões para baixo
            #
            # for i in range(6):
            #     if i < 3:
            #         button_x = button_x_left
            #     else:
            #         button_x = button_x_right
            #     button_rect = pygame.Rect(
            #         button_x,
            #         button_y + (i % 3) * (BUTTON_HEIGHT + button_spacing),
            #         BUTTON_WIDTH,
            #         BUTTON_HEIGHT,
            #     )
            #     pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
            #     pygame.draw.rect(screen, BUTTON_BORDER_COLOR, button_rect, 6)

    pygame.display.update()
