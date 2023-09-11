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

# Configurações do texto
TEXT_COLOR = (139, 69, 19)  # Marrom
TEXT_SIZE = 80

# Configurações do título do jogo
GAME_TITLE = "Scope: Mirando Certo"

# Caminho da imagem de fundo
BACKGROUND_IMAGE_PATH = R"image\fundo_menu.png"  # O caminho da imagem

# Caminho da imagem de fundo para a segunda tela
SECOND_PAGE_BACKGROUND_PATH = R"image\tela2.png"  # Caminho da nova imagem de fundo

# Criando a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tela de Início")

# Carregando a imagem de fundo
background_image = pygame.image.load(BACKGROUND_IMAGE_PATH).convert()
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
        SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
        SCREEN_HEIGHT - 180,
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

# Função para criar a segunda tela
def draw_second_page():
    # Carrega a imagem de fundo para a segunda tela
    second_page_background = pygame.image.load(SECOND_PAGE_BACKGROUND_PATH).convert()
    second_page_background = pygame.transform.scale(second_page_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Desenha a imagem de fundo da segunda tela
    screen.blit(second_page_background, (0, 0))

# Função para criar os botões na segunda tela
def draw_buttons_second_page():
    button_spacing = 20
    button_x_left = SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2  # Ajuste a posição inicial à esquerda
    button_x_right = 3 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2  # Ajuste a posição inicial à direita
    button_y = SCREEN_HEIGHT // 4 - BUTTON_HEIGHT // 2

    # Desenha 3 botões à esquerda
    for i in range(3):
        button_rect = pygame.Rect(
            button_x_left,
            button_y + i * (BUTTON_HEIGHT + button_spacing),  # Correção aqui
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )

        # Renderização do preenchimento do botão
        pygame.draw.rect(screen, (255, 255, 255), button_rect)

        # Renderização da borda do botão após o preenchimento
        button_border_surface = pygame.Surface((BUTTON_WIDTH + 6, BUTTON_HEIGHT + 6))
        button_border_surface.fill((255, 255, 255))
        button_border_rect = button_border_surface.get_rect(center=button_rect.center)
        screen.blit(button_border_surface, button_border_rect)

    button_y = SCREEN_HEIGHT // 4 - BUTTON_HEIGHT // 2  # Reinicializa a posição vertical

    # Desenha 3 botões à direita
    for i in range(3):
        button_rect = pygame.Rect(
            button_x_right,
            button_y + i * (BUTTON_HEIGHT + button_spacing),  # Correção aqui
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )

        # Renderização do preenchimento do botão
        pygame.draw.rect(screen, (255, 255, 255), button_rect)

        # Renderização da borda do botão após o preenchimento
        button_border_surface = pygame.Surface((BUTTON_WIDTH + 6, BUTTON_HEIGHT + 6))
        button_border_surface.fill((255, 255, 255))
        button_border_rect = button_border_surface.get_rect(center=button_rect.center)
        screen.blit(button_border_surface, button_border_rect)

    return button_x_left, button_x_right  # Retorna as posições

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

# Função para mudar de página
def change_page(page):
    global current_page
    current_page = page

# Função para processar o clique do mouse na segunda tela
def process_second_page_click(event, button_x_left, button_x_right):
    global selected_letter
    button_spacing = 20
    button_y = SCREEN_HEIGHT // 4 - BUTTON_HEIGHT // 2  # Correção aqui
    for i in range(6):
        if i < 3:
            button_x = button_x_left
        else:
            button_x = button_x_right
        button_rect = pygame.Rect(
            button_x,
            button_y + (i % 3) * (BUTTON_HEIGHT + button_spacing),  # Correção aqui
            BUTTON_WIDTH,
            BUTTON_HEIGHT,
        )
        if button_rect.collidepoint(event.pos):
            selected_letter = button_letter_mapping[i]
            print(f"Botão {selected_letter} clicado.")
            change_page("terceira_pagina")

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_page == "menu":
                button_rect = pygame.Rect(
                    SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2,
                    SCREEN_HEIGHT - 180,
                    BUTTON_WIDTH,
                    BUTTON_HEIGHT,
                )
                if button_rect.collidepoint(event.pos):
                    change_page("outra_pagina")
            elif current_page == "outra_pagina":
                process_second_page_click(event, button_x_left, button_x_right)

    screen.blit(background_image, (0, 0))

    if current_page == "menu":
        draw_text_with_borders(GAME_TITLE, TEXT_SIZE, TEXT_COLOR, (0, 0, 0), SCREEN_WIDTH // 2, 150)
        draw_button()
    elif current_page == "outra_pagina":
        draw_second_page()  # Desenha a segunda tela
        button_x_left, button_x_right = draw_buttons_second_page()  # Desenha os botões na segunda tela

    pygame.display.update()
