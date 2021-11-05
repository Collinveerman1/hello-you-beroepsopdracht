start = """
Het was een rustige dag rond de hoofdstad van Syrië. Tot er oppeens een luide knal klonk. 

Typ: volgende, om verder te gaan.
"""

oorlogbegint = """
We keken op het nieuws en er was en oorlog begonnen. We raakte in paniek en wisten niet wat we moesten doen.

Typ: volgende, om verder te gaan.
"""
inpakken = """
We hebben alle belangrijke spullen binnen no time gepakt en toen waren we klaar om te vluchten.
Je oom en vader willen vluchten. Wat kies je?

A. Je vader vlucht en jij blijft bij je familie.
B. Je vlucht met je oom.
"""

vadervlucht = """
Je vader vlucht en jij blijft met je familie in Sirië.
Jullie kunnen kiezen om te gaan schuilen of te gaan werken.
Wat kiezen jullie?

A. Werken
B. Schuilen
"""
vaderwerken = """
Je gaat werken om wat geld te verdienen om zo je familie te onderhouden.
Je vader heeft afgesproken om iedere dag te bellen.
Hij heeft gezegd dat hij jullie naar Nederland haalt.
Je kan ook sparen om zelf naar Nederland te gaan met je familie.
Wat kies je?

A. Wachten
B. Sparen
"""

vaderwacht = """
Je wacht tot je vader in Nederland aankomt en je naar Nederland haalt.

Typ: volgende, om verder te gaan.
"""

vaderwachtnl = """
Je komt succesvol in Nederland aan en je begint aan een nieuw mooi leven.
"""

vadersparen = """
Je werkt veel om je familie te onderhouden.
Uiteindelijk heb je genoeg geld om vliegtickets te kopen.

Typ: volgende, om verder te gaan.
"""

vadersparennl = """
Je komt aan in Nederland en je bent heel blij om je vader weer te zien.
Je begint aan een nieuw en mooi leven.
"""

vaderschuilen = """
Je gaat schuilen met je gezin terwijl je vader naar Nederland vlucht.
Je familie gaat ook schuilen. Waar ga je schuilen?

A. Thuis.
B. Bij je familie.
"""

schuilenfam = """
Je gaat schuilen met je familie in een kelder.
Er is genoeg eten om lang te overleven.

Typ: volgende, om verder te gaan.
"""
opgepaktinval = """
Oh nee! De terroristen breken binnen en hebben jullie gevonden.
Jullie worden allemaal opgepakt.
"""

schuilenthuis = """
Je gaat thuis in de kelder schuilen met je gezin.
Terwijl jullie daar zitten horen jullie allemaal knallen van geweren.

Typ: volgende, om verder te gaan.
"""

schuilenwacht = """
Jullie overleven de aanvallen en gaan daarna veilig met het vliegtuig naar Nederland waar je een mooi nieuw leven begint.
"""

oomvlucht = """ 
Je gaat met je oom mee naar buiten en neemt belangrijke spullen mee.
Je oom kent een paar mensen die ook willen vluchten.
Gaan jij en je oom alleen of met de groep mee?

A. Groep
B. Alleen
"""

oomgroep = """
Je oom, de groep en jij gaan samen vluchten naar Nederland.
Jullie komen bij een splitsing uit die 2 kanten op gaat.
Jullie kunnen met de boot vluchten of naar de volgende stad vluchten
Wat kies je?

A. Volgende stad
B. Boot
"""

groepstad = """
Je gaat met de groep naar de volgende stad toe.
Jullie lopen via een onbekende route en komen dan een paar vrachtwagenchauffeurs tegen.

Typ: volgende, om verder te gaan.
"""

stadsmokkel = """
Jullie worden door de chauffeurs meegesmokkeld naar Nederland.
Het kostte wel wat geld maar jullie ijn nu veilig.
Jij en je oom halen jkullie familie naar Nederland en woren heel gelukkig samen.
"""

oomalleen = """
Je gaat alleen met je oom vluchten.
Jullie komen aan bij een splitsing die naar de volgende stad gaat en naar een boot.
Welke weg kies je?

A. Volgende stad
B. Boot
"""

groepboot = """
Je gaat met de groep naar de boot.
Het is een kleine boot dus je weet niet of het gaat passen
Gelukkig kan iedereen mee en gaan jukie naar Nederland

Typ: volgende, om verder te gaan.
"""

opgepaktboot = """
Oh nee, de terroristen hebben jullie boot gekaapt en jullie worden allemaal opgepakt.
"""

oomstad = """
Je gaat met je oom naar de stad en proberen daar een weg te zoeken om dichter bij de grens te komen.

Typ: volgende, om verder te gaan.
"""

opgepakt = """
Oh nee, jullie worden gepakt door terroristen omdat jullie in een verboden gebied liepen.
"""

oomboot = """
Je oom en jij kiezen het pad van de boot.
Jullie stappen op de boot en gaan varen.

Typ: volgende, om verder te gaan.
"""

turkije = """
Na lang varen komen jullie aan in Turkije.
Jullie gaan hier door te liften naar Nederland.
Uiteindelijk mag jullie familie ook naar Nederland.
Jullie leven nog lang en gelukkig.
"""

print (start)

scriptinput = input()
if scriptinput == "volgende":
    print(oorlogbegint)
    scriptinput = input()
    if scriptinput == "volgende":
        print(inpakken)
        scriptinput = input()
        if scriptinput == "A" or scriptinput == "a":
            print(vadervlucht)
            scriptinput = input()
            if scriptinput == "A" or scriptinput == "a":
                print(vaderwerken)
                scriptinput = input()
                if scriptinput == "A" or scriptinput == "a":
                    print(vaderwacht)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(vaderwachtnl)
                elif scriptinput == "B" or scriptinput == "b":
                    print(vadersparen)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(vadersparennl)
            elif scriptinput == "B" or scriptinput == "b":
                print(vaderschuilen)
                scriptinput = input()
                if scriptinput == "A" or scriptinput == "a":
                    print(schuilenthuis)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(opgepaktinval)
                elif scriptinput == "B" or scriptinput == "b":
                    print(schuilenfam)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(schuilenwacht)
        elif scriptinput == "B" or scriptinput == "b":
            print(oomvlucht)
            scriptinput = input()
            if scriptinput == "A" or scriptinput == "a":
                print(oomgroep)
                scriptinput = input()
                if scriptinput == "A" or scriptinput == "a":
                    print(groepstad)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(stadsmokkel)
                elif scriptinput == "B" or scriptinput == "b":
                    print(groepboot)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(opgepaktboot)
            elif scriptinput == "B" or scriptinput == "b":
                print(oomalleen)
                scriptinput = input()
                if scriptinput == "A" or scriptinput == "a":
                    print(oomstad)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(opgepakt)
                elif scriptinput == "B" or scriptinput == "b":
                    print(oomboot)
                    scriptinput = input()
                    if scriptinput == "volgende":
                        print(turkije)

        
