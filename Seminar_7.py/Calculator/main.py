# Реализовать калькулятор
# main.py -> controller.py -> input_data.py -> 
# data_keeper.py -> functions.py -> logger.py -> 
# output_keeper.py

from functions import result
from input_data import inputData

a, znak, b = inputData()

print(result(znak, a, b))
