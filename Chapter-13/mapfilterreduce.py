from functools import reduce

#map example
l =[1,2,3,45,66]

square = lambda x : x*x

sqlist = map(square, l)
print(list(sqlist))

#filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

#reduce example

def sum(a, b):
    return a + b

mul = lambda x,y:x*y

total = reduce(sum, l)
print(reduce(mul, l))
print(total)