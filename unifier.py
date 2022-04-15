import formater


def calculate(text):
    result = 0
    order = formater.text_format(text)
    for element in order:
        result += element
    temp = f"{text}= {order}= {result}"
    return temp
