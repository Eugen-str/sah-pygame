import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
pygame.display.set_caption('Šah')
clock = pygame.time.Clock()
quit = False

def ploca_crtaj():
    (sirina, visina) = pygame.display.get_surface().get_size()

    screen.fill((18, 18, 18))

    if sirina > visina:
        kvad_sirina = visina / 8
        xpad = (sirina - visina)/2
        ypad = 0
    else:
        kvad_sirina = sirina / 8
        xpad = 0
        ypad = (visina - sirina)/2


    kvadrat = pygame.Surface((kvad_sirina, kvad_sirina))

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                kvadrat.fill((238,238,210))
                screen.blit(kvadrat, (i*kvad_sirina + xpad, j*kvad_sirina + ypad))
            else:
                kvadrat.fill((118,150,86))
                screen.blit(kvadrat, (i*kvad_sirina + xpad, j*kvad_sirina + ypad))
                

# GLAVNA PETLJA
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    ploca_crtaj()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()