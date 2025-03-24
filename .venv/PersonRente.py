from operator import truediv

import sterbetafel
import random
class PersonRente:

    def __init__(self, alter, sterbetafel: sterbetafel.Sterbetafel, rate):
        self.alter = alter
        self.i = 0
        self.lebt = True
        self.sterbetafel = sterbetafel
        self.rente = rate


    def calculateOutput(self):

        test = self.sterbetafel.getChanceFor(2023+self.i, self.alter)
        ## HIER BERECHNEN OB ER LEBT ODER STIRBT
        if self.diesOrNot(self.sterbetafel.getChanceFor(2023+self.i, self.alter)):

            self.lebt = False


        if self.lebt==False: return 0

        #Stattdessen berechnen wie Hoch die Rente ist oder so ka
        toReturn = self.rente



        self.i += 1
        if self.alter != 100:
            self.alter+= 1

        if self.alter >= 65:
            return toReturn
        else:
            return 0

    def diesOrNot (self, probability:float):
            guess = random.uniform(0, 1)

            if (guess <= probability):

                return True

            else: return False