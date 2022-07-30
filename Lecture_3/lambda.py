# def sum(x, y):
#     return x+y

# sum = lambda x, y: x+y + 1

def mult(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(lambda x, y: x+y + 1, 4, 5)