import PersonVersicherung
import sterbetafel
import PersonRente
import random
import pandas
import math

print("Start Simulation")

###Define Params
basis =  sterbetafel.Sterbetafel(r'''C:\Users\Chris\Desktop\Ella\Sterbetafel_Basisisszenario.csv''')
lang = sterbetafel.Sterbetafel(r'''C:\Users\Chris\Desktop\Ella\Sterbetafel_Langlebigkeitsszenario.csv''')
extrem = sterbetafel.Sterbetafel(r'''C:\Users\Chris\Desktop\Ella\Sterbetafel_Extremszenario.csv''')

wachstum = pandas.read_csv(r'''C:\Users\Chris\Desktop\Ella\gbm_mean_returns_head50.csv''')

listOfPeople = []
assets = 0

print("Build Lists!")

for person in range(0, 8000):
    alter = 65 #random.randint(20, 100)
    listOfPeople.append(PersonRente.PersonRente(alter, basis))

for person in range(0, 2000):
    alter = 30 #random.randint(20, 100)
    listOfPeople.append(PersonVersicherung.PersonVersicherung(alter, basis))

assets += len(listOfPeople) * 100000

print("start Simulating!")
for year in range (0, 35):
    ##hier kommt die Berechnung für die Zinsen von dem Jahr
    f: float = wachstum.loc[year + 1]["return"]
    exp: float = math.exp(f)
    assets = assets * math.exp(wachstum.loc[year + 1]["return"])

    leben_noch = 0
    for person in listOfPeople:
        assets -= person.calculateOutput()
        ## Formel 3
        if person.lebt == True:
            leben_noch += 1



    print("Jahr: " + str(2023+year) + " Assets: " + str(assets) + " Noch am Leben: " + str(leben_noch) )


#with open("ergebnis.csv", "a") as f:
 #   asd =  "asd " +  "\n"
  #  f.write(asd)
