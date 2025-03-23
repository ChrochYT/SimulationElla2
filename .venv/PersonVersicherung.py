from operator import truediv

import sterbetafel
import random
class PersonVersicherung:

    def __init__(self, alter, sterbetafel: sterbetafel.Sterbetafel):
        self.alter = alter
        self.i = 0
        self.lebt = True
        self.sterbetafel = sterbetafel
        self.a = 0
        for j in range(0, 35):
            self.a += (0.9900990099009901 ** (j+1)) * (1-self.sterbetafel.getChanceFor(2023+j,self.alter+j)) * (self.sterbetafel.getChanceFor(2023+j,self.alter+j+1))

        self.auszahlung = 100000 / self.a

    def calculateOutput(self):
        if self.lebt == False: return 0


        #Stattdessen berechnen wie Hoch die Rente ist oder so ka
        toReturn = self.auszahlung

        ## HIER BERECHNEN OB ER LEBT ODER STIRBT
        if self.diesOrNot(self.sterbetafel.getChanceFor(2023+self.i, self.alter)):
            self.lebt = False
            if(self.alter<= 65 ):
                return toReturn

        self.i += 1
        if self.alter != 100:
            self.alter+= 1
        return 0

    def diesOrNot (self, probability:float):
            guess = random.uniform(0, 1)
