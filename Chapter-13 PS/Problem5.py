from functools import reduce

a = [32,30,64,54,3432,341,21]

def max(a,b):
    if(a>b):
        return a
    return b

print(reduce(max, a))