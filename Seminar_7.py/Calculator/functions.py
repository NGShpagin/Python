def result(znak, a, b):
    znaki = {"+": a+b, "-": a-b, '*': a*b, '/': a / b}
    for i in znaki.keys():
        if i == znak:
            return f'Результат вычисления: {znaki[i]}'