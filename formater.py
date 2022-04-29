import my_math


def text_format(text):
    """
    Der Text wird in seine einzelnen Befehle aufgespalten, zu die_format geschickt und danach an unifier zurückgegeben
    """
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
    """
    Einzelne Befehle werden formatiert und an my_math.wuerfeln übergeben
    """
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
            number = my_math.wuerfeln(int(die[0]), int(die[1]))
            temp.extend(number)
        # Die Modifier werden Separat gehandelt
        else:
            temp.append(int(each))
    return temp
