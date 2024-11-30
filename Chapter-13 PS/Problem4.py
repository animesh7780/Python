def divisible(n):
    if(n%5 == 0 ):
        return True
    return False

a = [32,30,64,54,3432,341,21]

f = list(filter(divisible, a))
print(f)