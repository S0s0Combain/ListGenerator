from os import system
import random
from warnings import catch_warnings
def list_generator(dimension):
    try:
        list=[]
        for i in range(dimension):
            list.append(random.randint(5,1400))
        return list
    except:
        print('Uncorrect data')
        exit()
print(list_generator(24))
