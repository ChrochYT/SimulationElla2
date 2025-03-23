import pandas

class Sterbetafel:
    def __init__(self, file):
        self.file = file
        self.fromCsv = pandas.read_csv(file)


    def getChanceFor(self, actJahr, alter):
        return self.fromCsv.loc[alter][str(actJahr)]

