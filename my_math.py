
import random

# Hier wird eingegeben welche Art von Würfel und wie viele gewürfelt werden.
def wuerfeln(anzahl, typ):
    liste = []
    for i in range(anzahl):
        temp = random.randint(1, typ)
        liste.append(temp)
    return liste
