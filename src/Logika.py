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

    def napraviPotez(self, potez):
        self.ploca[potez.redPoc][potez.linPoc] = "--"
        self.ploca[potez.redZav][potez.linZav] = potez.figura

class Potez:
    def __init__(self, kvPocetak, kvKraj, ploca):
        #red (1-8), linija (a-h)
        self.redPoc = kvPocetak[1]
        self.linPoc = kvPocetak[0]

        self.redZav = kvKraj[1]
        self.linZav = kvKraj[0]

        self.figura = ploca[self.redPoc][self.linPoc]
    
    def genNotacija(self):
        redovi = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
        