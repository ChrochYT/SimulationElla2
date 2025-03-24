import PersonVersicherung
import sterbetafel
import PersonRente
import random
import pandas
import math

###Define Params
basis = sterbetafel.Sterbetafel(r'''C:\Users\Chroc\Desktop\forElla\Sterbetafel_Basisisszenario.csv''')
lang = sterbetafel.Sterbetafel(r'''C:\Users\Chroc\Desktop\forElla\Sterbetafel_Langlebigkeitsszenario.csv''')
extrem = sterbetafel.Sterbetafel(r'''C:\Users\Chroc\Desktop\forElla\Sterbetafel_Extremszenario.csv''')

wachstum = pandas.read_csv(r'''C:\Users\Chroc\Desktop\forElla\gbm_mean_returns_head50.csv''')

i0 = 100000


def getRenteForAge(alter):
    a = 0
    for j in range(1, 36):
        survival_prob = math.prod(((1 - basis.getChanceFor(2023 + k, alter + k)) for k in range(j)))

        a += survival_prob * (0.9900990099009901 ** j)

    return i0 / a

def getAuszahlungForAge(alter):
    b = 0
    for j in range(0, 35):
        survival_prob = math.prod((1 - basis.getChanceFor(2023 + k, alter + k)) for k in range(j))

        death_prob = basis.getChanceFor(2023 + j, alter + j)

        b += survival_prob * death_prob * (0.9900990099009901 ** (j + 1))

    return i0 / b

rente = getRenteForAge(65)
auszahlung = getAuszahlungForAge(30)

#print("Start Simulation")

for x in range(0, 1000):
    listOfPeople = []
    assets = 0

    #print("Build Lists!")

    for person in range(0, 80):
        alter = 65  # random.randint(20, 100)
        listOfPeople.append(PersonRente.PersonRente(alter, basis, rente))

    for person in range(0, 20):
        alter = 30  # random.randint(20, 100)
        listOfPeople.append(PersonVersicherung.PersonVersicherung(alter, basis, auszahlung))

    assets += len(listOfPeople) * i0
    assets -= 80 * rente
    #print("start Simulating!")
    for year in range(0, 35):
        ##hier kommt die Berechnung für die Zinsen von dem Jahr
        f: float = wachstum.loc[year + 1]["return"]
        exp: float = math.exp(f)

        leben_noch = 0
        for person in listOfPeople:
            assets -= person.calculateOutput()
            ## Formel 3
            if person.lebt == True:
                leben_noch += 1
            else:
                listOfPeople.remove(person)

        assets = assets * math.exp(wachstum.loc[year + 1]["return"])
         #math.exp(wachstum.loc[year + 1]["return"])
        #print("Jahr: " + str(2023 + year) + " Assets: " + str(assets) + " Noch am Leben: " + str(leben_noch))
    print(assets / 100)


# with open("ergebnis.csv", "a") as f:
#   asd =  "asd " +  "\n"
#  f.write(asd)
