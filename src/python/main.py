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
TEXT_SIZE = 70

# Configurações do título do jogo
GAME_TITLE = "Scope: Mirando Certo"

# Caminho da imagem de fundo
BACKGROUND_IMAGE_PATH = r"image\fundo_menu.png"  # O caminho da imagem

# Caminho da imagem de fundo para a segunda tela
SECOND_PAGE_BACKGROUND_PATH = r"image\tela2.png"  # Caminho da nova imagem de fundo

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

    # Renderização da borda
    border_surface = font.render(text, True, border_color)
    border_rect = border_surface.get_rect(center=text_surface.get_rect(center=(x + 2, y + 2)).center)

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


# Variável de controle para determinar a página
current_page = "menu"


# Função para mudar de página
def change_page(page):
    global current_page
    current_page = page


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

    screen.blit(background_image, (0, 0))

    if current_page == "menu":
        draw_text_with_borders(GAME_TITLE, TEXT_SIZE, TEXT_COLOR, (0, 0, 0), SCREEN_WIDTH // 2, 150)
        draw_button()
    elif current_page == "outra_pagina":
        draw_second_page()  # Desenha a segunda tela

    pygame.display.update()
