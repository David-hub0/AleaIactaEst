
import formater


def calculate(text):
    result = 0
    order = formater.text_format(text)
    for element in order:
        result += element
    ausgabetext = f": {text} = {order} = {result}"
    if len(ausgabetext)>2000:
        ausgabetext= f"Die detaillierte Antwort besteht aus {len(ausgabetext)} Zeichen und ist damit zu lang. Das " \
                     f"Ergebnis ist {result} "
    return ausgabetext
