import pygame
from gun import Gun
import controls
from pygame.sprite import Group


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("SnenegrBlack")
    bg_color = (0, 105, 60)
    gun = Gun(screen)
    bullets = Group()

    fon = pygame.image.load('image/y.webp')
    rect7 = fon.get_rect()


    while True:
        screen.blit(fon, rect7)
        controls.events(screen,gun,bullets)
        gun.update_gun()
        gun.update_gun2()
        controls.update(bg_color,screen,gun, bullets)
        controls.delete(bullets)
        print(gun.rect.centerx)
        print(gun.rect.centery)



















run()