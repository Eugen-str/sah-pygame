class Stanjeigre:
    def __init__(self):
        self.ploca = [
            ["ct", "cs", "cl", "cq", "ck", "cl", "cs", "ct"],
            ["cp", "cp", "cp", "cp", "cp", "cp", "cp", "cp"],
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

                    # print(potezi[len(potezi) - 1].potezID)

        return potezi

    def legalniPijun(self, red, linija, potezi):
        if self.bijeliNaPotezu:
            k = 1
        else:
            k = -1
        potezi.append(Potez((linija, red), (linija, red - 1*k), self.ploca))
        if red == 6 and self.bijeliNaPotezu or red == 1 and not self.bijeliNaPotezu:
            potezi.append(Potez((linija, red), (linija, red - 2*k), self.ploca))

    def legalniTop(self, red, linija, potezi):
        pass

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
