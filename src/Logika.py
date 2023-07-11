class stanjeIgre:
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

class Potez:
    def __init__(self, kvPocetak, kvKraj, ploca):
        # red (1-8), linija (a-h)
        self.redPoc = kvPocetak[1]
        self.linPoc = kvPocetak[0]

        self.redZav = kvKraj[1]
        self.linZav = kvKraj[0]

        self.uzetaFigura = ploca[self.redZav][self.linZav]
        self.figura = ploca[self.redPoc][self.linPoc]

    def genNotacija(self, stanje: stanjeIgre):
        uzeto = ""
        if self.uzetaFigura != "--":
            uzeto = "x"

        return str(stanje.brojPoteza) + ". " + self.figura[1].upper() + uzeto + chr(self.linZav + ord('a')) + str(
            self.redZav + 1)
