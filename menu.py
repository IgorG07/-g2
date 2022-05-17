import pygame
import sys
pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
color = (0, 0, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('ПОШЁЛ ИГРАТЬ', True, color)
text2 = smallfont.render('Выход', True, color)
text3 = smallfont.render('Об игре', True, color)
while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()



        if ev.type == pygame.MOUSEBUTTONDOWN:
            if 230 <= mouse[0] <= 500 and 334 <= mouse[1] <= 393:
                pygame.quit()
            if 230 <= mouse[0] <= 500 and 280 <= mouse[1] <= 317:
                pygame.quit()
            if  230 <= mouse[0] <=  500 and  183 <= mouse[1] <=  223:
                pygame.quit()
                import main
    screen.fill((60, 25, 60))
    mouse = pygame.mouse.get_pos()
    print("x =", mouse[0],'y =', mouse[1])
    if  230 <= mouse[0] <=  500 and  183 <= mouse[1] <=  223:
        pygame.draw.rect(screen, color_light, [ 230,   184, 270, 40])

    else:
        pygame.draw.rect(screen, color_dark, [ 230, 184, 270, 40])




    if  230 <= mouse[0] <=  500 and  280 <= mouse[1] <=  317:


        pygame.draw.rect(screen, color_light, [ 230,   280, 270, 40])

    else:
        pygame.draw.rect(screen, color_dark, [ 230, 280, 270, 40])




    if  230 <= mouse[0] <=  500 and  334 <= mouse[1] <=  393:


        pygame.draw.rect(screen, color_light, [ 230,   335, 270, 60])

    else:
        pygame.draw.rect(screen, color_dark, [ 230, 335, 270, 60])

    screen.blit(text, ( 243,  187))
    screen.blit(text2, ( 313,  283))
    screen.blit(text3, (300, 345))

    pygame.display.update()