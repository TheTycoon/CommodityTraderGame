import pygame
import settings


def draw_text(window, text, size, color, x, y, centered):
    font = pygame.font.Font(settings.FONT, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.x = x
    text_rect.y = y
    if centered:
        text_rect.midtop = (x, y)
    window.blit(text_surface, text_rect)


