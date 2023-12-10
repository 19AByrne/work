import pygame
from sys import exit
def display_cookies():
    cookie_text = font.render(f"Cookies: {cookies}", False, (64,64,64))
    cookie_text_rect = cookie_text.get_rect(center = (scwidth/2, scheight/4))
    screen.blit(cookie_text,cookie_text_rect)
pygame.init()
scwidth = 1280
scheight = 720
screen = pygame.display.set_mode((scwidth,scheight))
running = True
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf', 100)

cookie = pygame.image.load('graphics/cookie.png').convert_alpha()
cookie_rect = cookie.get_rect(center=(scwidth/2,scheight/2))

cookies = 0
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cookie_rect.collidepoint(event.pos):
                cookies+=1
    screen.fill('#411900')
    screen.blit(cookie,cookie_rect)
    display_cookies()
    pygame.display.update()
    