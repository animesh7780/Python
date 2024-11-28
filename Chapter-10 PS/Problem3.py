class one:
    a = 10

o = one()
o.a = 20
print(o.a)#prints instance attribute becuase it is not class attribute
print(one.a)#prints class attribute
