import pygame
import Logika

from Logika import stanjeIgre

DIMENZIJA = 1000
KVADRAT = DIMENZIJA/8
SLIKE = {}

def ucitajSlike():
    figure = ["bp", "bt", "bs", "bl", "bk", "bq", "cp", "ct", "cs", "cl", "cq", "ck"]
    for figura in figure:
        SLIKE[figura] = pygame.transform.scale(pygame.image.load("slike/" + figura + ".png"), (KVADRAT, KVADRAT))

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

    screen = pygame.display.set_mode((DIMENZIJA, DIMENZIJA))
    pygame.display.set_caption('Šah')
    clock = pygame.time.Clock()
    quit = False

    odabrano = False

    ucitajSlike()

    stanje = stanjeIgre()

    while not quit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                misPoz = pygame.mouse.get_pos()
                red = int(misPoz[0] // KVADRAT)
                linija = int(misPoz[1] // KVADRAT)

                if not odabrano:
                    prviPotez = (red, linija)

                    odabrano = True
                elif(odabrano and prviPotez != (red, linija)):
                    drugiPotez = (red, linija)
                    
                    potez = Logika.Potez(prviPotez, drugiPotez, stanje.ploca)
                    stanje.napraviPotez(potez)

                    odabrano = False

        nacrtajPlocu(screen)
        nacrtajFigure(screen, stanje.ploca)

        pygame.display.flip()
        clock.tick(24)

    pygame.quit()



if __name__ == "__main__":
    main()