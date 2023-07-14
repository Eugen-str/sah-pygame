class Stanjeigre:
    def __init__(self):
        self.ploca = [
            ["ct", "cs", "cl", "cq", "ck", "cl", "cs", "ct"],
            ["cp", "cp", "cp", "cp", "cp", "cp", "cp", "cp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bt", "bs", "bl", "bq", "bk", "bl", "bs", "bt"]
        ]
        self.brojPoteza = 0
        self.bijeliNaPotezu = True
        self.listaPoteza = []

    def napraviPotez(self, potez):
        self.brojPoteza += 1

        self.ploca[potez.redPoc][potez.linPoc] = "--"
        self.ploca[potez.redZav][potez.linZav] = potez.figura

        self.listaPoteza.append(potez)
        self.bijeliNaPotezu = not self.bijeliNaPotezu

    def vratiPotez(self):
        if len(self.listaPoteza) > 0:
            potez = self.listaPoteza.pop()

            self.ploca[potez.redZav][potez.linZav] = potez.uzetaFigura
            self.ploca[potez.redPoc][potez.linPoc] = potez.figura

            self.bijeliNaPotezu = not self.bijeliNaPotezu

    def legalniPotezi(self):
        return self.pseudoLegalniPotezi()  # zasad...

    # generiranje svih pseudolegalnih poteza (pseudolegalni - bez uzimanja šaha i šah-mata u obzir)
    def pseudoLegalniPotezi(self):
        potezi = []

        for i in range(8):
            for j in range(8):
                if self.ploca[i][j][0] == "b" and self.bijeliNaPotezu or self.ploca[i][j][0] == "c" and \
                        not self.bijeliNaPotezu:
                    figura = self.ploca[i][j][1]

                    metode = {"p": self.legalniPijun, "s": self.legalniSkakac,
                              "t": self.legalniTop, "k": self.legalniKralj,
                              "l": self.legalniLovac, "q": self.legalniKraljica}

                    metode[figura](i, j, potezi)

        return potezi

    # metoda za dodavanje svih legalnih poteza pijuna (bez en-passanta i promoviranja)
    def legalniPijun(self, red, linija, potezi):
        if self.bijeliNaPotezu:
            k = 1
            c = "b"
        else:
            k = -1
            c = "c"

        if red != 7 and red != 0:
            if self.ploca[red - k][linija] == "--":
                potezi.append(Potez((linija, red), (linija, red - k), self.ploca))

            if linija > 0 and self.ploca[red - k][linija - 1] != "--" and self.ploca[red - k][linija - 1][0] != c:
                potezi.append(Potez((linija, red), (linija - 1, red - k), self.ploca))

            if linija < 7 and self.ploca[red - k][linija + 1] != "--" and self.ploca[red - k][linija + 1][0] != c:
                potezi.append(Potez((linija, red), (linija + 1, red - k), self.ploca))

            if (red == 1 and not self.bijeliNaPotezu or red == 6 and self.bijeliNaPotezu) and \
                    self.ploca[red - k][linija] == "--" and self.ploca[red - 2 * k][linija] == "--":
                potezi.append(Potez((linija, red), (linija, red - 2 * k), self.ploca))

    def legalniTop(self, red, linija, potezi):
        c = "b" if self.bijeliNaPotezu else "c"

        direkcije = ((1, 0), (0, 1), (-1, 0), (0, -1))

        for d in direkcije:
            for i in range(1, 8):
                zavLin = linija + i*d[0]
                zavRed = red + i*d[1]

                if 0 <= zavLin <= 7 and 0 <= zavRed <= 7:
                    if self.ploca[zavRed][zavLin] == "--":
                        potezi.append(Potez((linija, red), (zavLin, zavRed), self.ploca))
                    elif self.ploca[zavRed][zavLin] != c:
                        potezi.append(Potez((linija, red), (zavLin, zavRed), self.ploca))
                        break
                    else:
                        break
                else:
                    break

#######################
        """
        for i in range(linija + 1, 8, 1):
            if self.ploca[red][i] == "--":
                potezi.append(Potez((linija, red), (i, red), self.ploca))
            elif self.ploca[red][i][0] != c:
                potezi.append(Potez((linija, red), (i, red), self.ploca))
                break
            else:
                break

        for i in range(linija - 1, -1, -1):
            if self.ploca[red][i] == "--":
                potezi.append(Potez((linija, red), (i, red), self.ploca))
            elif self.ploca[red][i][0] != c:
                potezi.append(Potez((linija, red), (i, red), self.ploca))
                break
            else:
                break

        for i in range(red + 1, 8, 1):
            if self.ploca[i][linija] == "--":
                potezi.append(Potez((linija, red), (linija, i), self.ploca))
            elif self.ploca[i][linija][0] != c:
                potezi.append(Potez((linija, red), (linija, i), self.ploca))
                break
            else:
                break

        for i in range(red - 1, -1, -1):
            if self.ploca[i][linija] == "--":
                potezi.append(Potez((linija, red), (linija, i), self.ploca))
            elif self.ploca[i][linija][0] != c:
                potezi.append(Potez((linija, red), (linija, i), self.ploca))
                break
            else:
                break
        """

    def legalniKraljica(self, red, linija, potezi):
        pass

    def legalniKralj(self, red, linija, potezi):
        pass

    def legalniLovac(self, red, linija, potezi):
        pass

    def legalniSkakac(self, red, linija, potezi):
        pass


class Potez:
    def __init__(self, kvPocetak, kvKraj, ploca):
        # red (1-8), linija (a-h)
        self.redPoc = kvPocetak[1]
        self.linPoc = kvPocetak[0]

        self.redZav = kvKraj[1]
        self.linZav = kvKraj[0]

        self.uzetaFigura = ploca[self.redZav][self.linZav]
        self.figura = ploca[self.redPoc][self.linPoc]

        self.potezID = self.redPoc * 1000 + self.linPoc * 100 + self.redZav * 10 + self.linZav

    def __eq__(self, other):
        if isinstance(other, Potez):
            return self.potezID == other.potezID
        return False

    def genNotacija(self, stanje: Stanjeigre):
        uzeto = ""
        if self.uzetaFigura != "--":
            uzeto = "x"

        return str(stanje.brojPoteza) + ". " + self.figura[1].upper() + uzeto + chr(self.linZav + ord('a')) + str(
            self.redZav + 1)
