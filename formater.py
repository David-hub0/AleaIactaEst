import my_math


def text_format(text):
    # Der Befehl '!die' wird entfernt.
    orderbody = text.split('!DIE ')
    rest = orderbody[1]

    # Falls mehrere Würfel aneinander gehangen werden wird das formatiert
    # mehrere Befehle werden am '+' aufgeteilt
    if '+' in rest:
        liste = []
        temp = rest.split('+')
        tempNoD = die_format(temp)
    # Edgecase für den Fall, dass es nur einen Befehl gibt
    else:
        liste = []
        tempNoD = die_format(rest)
    return tempNoD


def die_format(text):
    temp = []
    # Dynamischer Typ von Text wird der Listen Typ aufgezwungen
    if not isinstance(text, list):
        text = [text]
    # Den Unterbefehlen werden Werte zugewiesen
    for each in text:
        # Jeder Würfel-Befehl wird in Anzahl der Wiederholungen und Typ des Würfels zerlegt und an my_math.wuerfeln
        # gegeben
        if 'D' in each:
            die = each.split('D')
            temp.extend(my_math.wuerfeln(int(die[0]), int(die[1])))
        # Die Modifier werden Separat gehandelt
        else:
            temp.append(int(each))
    return temp
