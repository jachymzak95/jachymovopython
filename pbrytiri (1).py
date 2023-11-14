import random

class Valecnik:
    
    def __init__(self, jmeno, HP, ATK, DEF, zbran):
        self.jmeno = jmeno
        self._HP = HP
        self._ATK = ATK
        self.DEF = DEF
        self.zbran = zbran
    
    def zautoc(self, protivnik):
        return self.ATK + self.zbran.ATK - protivnik.DEF
    
    def __str__(self):
        return f"Jmeno: {self.jmeno}, HP: {self._HP}, zbran: {self.zbran}"
    
    @property
    def HP(self):
        return self._HP
    
    @HP.setter
    def HP(self,nove_HP):
        if nove_HP < 0:
            self._HP = 0
        else:
            self._HP = nove_HP

    @property
    def ATK(self):
        if ((self._ATK + self.zbran.ATK) + (self._ATK*(random.randint(0,2)/10))) > self.DEF:
            self._ATK = self._ATK - (self._ATK*(random.randint(0,2)/10))
            return self._ATK
        else:
            self._ATK += 10
            return self._ATK 

class Cigos(Valecnik):
    
    def __str__(self):
        return f"Jmeno: {self.jmeno}, HP: {self._HP}, zbran: {self.zbran}"
    
    def __init__(self, jmeno, HP, ATK, DEF, zbran):
        super().__init__(jmeno, HP, ATK, DEF, zbran)
        
        
class Zbran:
    
    def __init__(self, jmeno, ATK):
        self.jmeno = jmeno
        self._ATK = ATK
    
    def __str__(self):
        return self.jmeno
    
    @property
    def ATK(self):
            self._ATK = self._ATK - (self._ATK*(random.randint(0,2)/10))
            return self._ATK
    
class Luk(Zbran):
    def __init__(self, jmeno, ATK, sila_vystrelu):
        super().__init__(jmeno, ATK)
        self.sila_vystrelu = sila_vystrelu
        
class Pouzite_pleny(Zbran):
    def __init__(self, jmeno, ATK, smradlavost):
        super().__init__(jmeno, ATK)
        self.smradlavost = smradlavost
        
class Katapult(Zbran):
    def __init__(self, jmeno, ATK, hmotnost_naloze):
        super().__init__(jmeno, ATK)
        self.hmotnost_naloze = hmotnost_naloze

class Mec(Zbran):
    def __init__(self, jmeno, ATK, ostrost_cepele):
        super().__init__(jmeno, ATK)
        self.ostrost_cepele = ostrost_cepele

class Turnaj:
    
    def __init__(self):
        self.seznam_rytiru = []
    
    def registrace(self, rytir):
        self.seznam_rytiru.append(rytir)
    
    def duel(self):
        r1 = random.choice(self.seznam_rytiru)
        r2 = random.choice(self.seznam_rytiru)
        while r1 == r2:
            r1 = random.choice(self.seznam_rytiru)
            r2 = random.choice(self.seznam_rytiru)
        while r1.HP > 0 and r2.HP > 0:
            r2.HP = r2.HP - r1.zautoc(r2)
            r1.HP = r1.HP - r2.zautoc(r1)
        if r1.HP == 0 and r2.HP == 0:
            print("remíza")
        elif r1.HP == 0:
            self.seznam_rytiru.remove(r1)
            print(f"Vitez: {r2}")
        elif r2.HP == 0:
            self.seznam_rytiru.remove(r2)
            print(f"Vitez: {r1}")


def main():
       
    turnaj = Turnaj()
    nic = Zbran("nemam nic more", 0)
    dragon_slayer = Mec("Dragonslayer", 80, 100)
    Radioactive_waste_collector = Katapult("Castle destroyer 5000", 80, 100)
    guts = Valecnik("Guts", HP=400, ATK=30, DEF=25, zbran=dragon_slayer)
    griffith = Valecnik("Griffith", HP=400, ATK=30, DEF=25, zbran=Radioactive_waste_collector)
    
    Laco = Cigos("Laco", HP = 10, ATK = 400, DEF = 80, zbran = nic)
    
    turnaj.registrace(guts)
    turnaj.registrace(griffith)

    if random.random() > 0.5:
        krade_od = random.choice(turnaj.seznam_rytiru)
        if Laco.ATK > krade_od.ATK:
            krade_od.zbran, Laco.zbran = Laco.zbran, krade_od.zbran
            print(f"{krade_od.jmeno}ovo zbran ukradl cigos, smula")
   
    print("Ucastnici turnaje:")
    print(guts, griffith, Laco)
    
    turnaj.duel()
    
    print("Finalni stav:")
    print(guts, griffith, Laco)
    
main()