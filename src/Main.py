import pygame
import Logika

from Logika import Stanjeigre

MAX_FPS = 20
DIMENZIJA = 800
KVADRAT = DIMENZIJA / 8
SLIKE = {}

BIJELA = (238, 238, 210)
CRNA = (118, 150, 86)


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
                kvadrat.fill(BIJELA)
                screen.blit(kvadrat, (i * KVADRAT, j * KVADRAT))
            else:
                kvadrat.fill(CRNA)
                screen.blit(kvadrat, (i * KVADRAT, j * KVADRAT))

            if j == 0:
                screen.blit(font.render("{}".format(abs(8 - i)), True, (18, 18, 18)), (0, i * KVADRAT))
            if i == 7:
                screen.blit(font.render("{}".format(chr(j + ord('a'))), True, (18, 18, 18)),
                            (j * KVADRAT, DIMENZIJA - KVADRAT / 3))


# crtanje "osjenčavanja" podloge ispod mogucih poteza za sve figure na ploči
def nacrtajSveMogucePoteze(ekran, legalniPotezi):
    kvadrat = pygame.Surface((KVADRAT, KVADRAT))
    for potez in legalniPotezi:
        kvadrat.fill((255, 50, 50))
        ekran.blit(kvadrat, (potez.linZav * KVADRAT, potez.redZav * KVADRAT))
        kvadrat.fill((160, 40, 40))
        ekran.blit(kvadrat, (potez.linPoc * KVADRAT, potez.redPoc * KVADRAT))


# crtanje "osjenčavanja" podloge ispod mogucih poteza za odabranu figuru
def nacrtajPotez(ekran, legalniPotezi, pocPotez):
    linPotez, redPotez = pocPotez

    kvadrat = pygame.Surface((KVADRAT, KVADRAT))
    for p in legalniPotezi:
        if p.linPoc == linPotez and p.redPoc == redPotez:
            kvadrat.fill((255, 50, 50))
            ekran.blit(kvadrat, (p.linZav * KVADRAT, p.redZav * KVADRAT))
            kvadrat.fill((160, 40, 40))
            ekran.blit(kvadrat, (p.linPoc * KVADRAT, p.redPoc * KVADRAT))


def nacrtajProsliPotez(ekran, listaPoteza):
    zadnjiPotez = listaPoteza[len(listaPoteza) - 1]

    kvadrat = pygame.Surface((KVADRAT, KVADRAT))
    if (zadnjiPotez.linPoc + zadnjiPotez.redPoc) % 2 == 0:
        boja = (199, 227, 134)
    else:
        boja = (227, 255, 161)
    kvadrat.fill(boja)
    ekran.blit(kvadrat, (zadnjiPotez.linZav * KVADRAT, zadnjiPotez.redZav * KVADRAT))

    if (zadnjiPotez.linZav + zadnjiPotez.redZav) % 2 == 0:
        boja = (199, 227, 134)
    else:
        boja = (227, 255, 161)
    kvadrat.fill(boja)
    ekran.blit(kvadrat, (zadnjiPotez.linPoc * KVADRAT, zadnjiPotez.redPoc * KVADRAT))


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
    stanje = Stanjeigre()
    legalniPotezi = stanje.legalniPotezi()
    potez = ()

    # provjera ispravnog broja mogućih poteza
    # print(len(legalniPotezi))

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

                    odabrano = False

                    if potez in legalniPotezi:
                        stanje.napraviPotez(potez)
                        print(potez.genNotacija(stanje))
                        legalniPotezi = stanje.legalniPotezi()
                    else:
                        prviPotez = drugiPotez
                        odabrano = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    stanje.vratiPotez()
        # kraj petlje za evente

        nacrtajPlocu(ekran, font)

        if len(stanje.listaPoteza) > 0:
            nacrtajProsliPotez(ekran, stanje.listaPoteza)

        # nacrtajSveMogucePoteze(ekran, legalniPotezi)
        if odabrano:
            nacrtajPotez(ekran, legalniPotezi, prviPotez)

        nacrtajFigure(ekran, stanje.ploca)

        pygame.display.flip()
        sat.tick(MAX_FPS)
    # kraj glavne petlje
    pygame.quit()


if __name__ == "__main__":
    main()
