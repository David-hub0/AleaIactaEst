import random


def wuerfeln(anzahl, typ):
    """
    Hier wird eingegeben welche Art von Würfel und wie viele gewürfelt werden.
    """
    liste = []
    for i in range(anzahl):
        temp = random.randint(1, typ)
        liste.append(temp)
    return liste
