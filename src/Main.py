import pygame
import Logika

from Logika import stanjeIgre

MAX_FPS = 20
DIMENZIJA = 800
KVADRAT = DIMENZIJA / 8
SLIKE = {}

def ucitajSlike():
    figure = ["bp", "bt", "bs", "bl", "bk", "bq", "cp", "ct", "cs", "cl", "cq", "ck"]
    for figura in figure:
        SLIKE[figura] = pygame.transform.scale(pygame.image.load("../slike/" + figura + ".png"), (KVADRAT, KVADRAT))


def nacrtajFigure(screen, ploca):
    for i in range(8):
        for j in range(8):
            figura = ploca[j][i]
            if figura != "--":
                screen.blit(SLIKE[figura], pygame.Rect(i * KVADRAT, j * KVADRAT, KVADRAT, KVADRAT))


def nacrtajPlocu(screen, font):
    kvadrat = pygame.Surface((KVADRAT, KVADRAT))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                kvadrat.fill((238, 238, 210))
                screen.blit(kvadrat, (i * KVADRAT, j * KVADRAT))
            else:
                kvadrat.fill((118, 150, 86))
                screen.blit(kvadrat, (i * KVADRAT, j * KVADRAT))

            if j == 0:
                screen.blit(font.render("{}".format(i + 1), True, (18, 18, 18)), (0, i * KVADRAT))
            if i == 7:
                screen.blit(font.render("{}".format(chr(j + ord('a'))), True, (18, 18, 18)), (j * KVADRAT, DIMENZIJA - KVADRAT / 3))


def main():
    pygame.init()

    # inicijaliziranje pygame stvari
    ekran = pygame.display.set_mode((DIMENZIJA, DIMENZIJA))
    pygame.display.set_caption('Šah')
    sat = pygame.time.Clock()
    # font preuzet sa https://www.jetbrains.com/lp/mono/
    font = pygame.font.Font('../font/JetBrainsMono-Regular.ttf', int(KVADRAT // 3.5))

    ucitajSlike()
    kraj = False

    # inicijaliziranje početnog stanja igre
    stanje = stanjeIgre()
    legalniPotezi = stanje.legalniPotezi()

    odabrano = False

    prviPotez = ()




    while not kraj:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kraj = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                misPoz = pygame.mouse.get_pos()
                red = int(misPoz[0] // KVADRAT)
                linija = int(misPoz[1] // KVADRAT)

                if not odabrano:
                    prviPotez = (red, linija)

                    odabrano = True
                elif odabrano and prviPotez == (red, linija):
                    prviPotez = ()

                    odabrano = False
                elif odabrano:
                    drugiPotez = (red, linija)

                    potez = Logika.Potez(prviPotez, drugiPotez, stanje.ploca)

                    if potez in legalniPotezi:
                        stanje.napraviPotez(potez)
                        print(potez.genNotacija(stanje))

                    prviPotez = ()
                    odabrano = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    stanje.vratiPotez()



        nacrtajPlocu(ekran, font)
        nacrtajFigure(ekran, stanje.ploca)

        pygame.display.flip()
        sat.tick(MAX_FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
