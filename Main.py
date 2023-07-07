import pygame
from Logika import *

KVADRAT = 100
SLIKE = {}

def ucitajSlike():
    figure = ["bp", "bt", "bs", "bl", "bk", "bq", "cp", "ct", "cs", "cl", "cq", "ck"]
    for figura in figure:
        SLIKE[figura] = pygame.transform.scale(pygame.image.load("./slike/" + figura + ".png"), (KVADRAT, KVADRAT))

def nacrtajFigure(screen, ploca):
    for i in range(8):
        for j in range(8):
            figura = ploca[j][i]
            if figura != "--":
                screen.blit(SLIKE[figura], pygame.Rect(i * KVADRAT, j*KVADRAT, KVADRAT, KVADRAT))

def nacrtajPlocu(screen):
    kvadrat = pygame.Surface((KVADRAT, KVADRAT))
    for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    kvadrat.fill((238,238,210))
                    screen.blit(kvadrat, (i*KVADRAT, j*KVADRAT))
                else:
                    kvadrat.fill((118,150,86))
                    screen.blit(kvadrat, (i*KVADRAT, j*KVADRAT))

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Šah')
    clock = pygame.time.Clock()
    quit = False

    ucitajSlike()

    ploca = Ploca()

    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True

        nacrtajPlocu(screen)
        nacrtajFigure(screen, ploca.ploca)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()



if __name__ == "__main__":
    main()