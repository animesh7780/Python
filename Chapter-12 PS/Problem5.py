n = 9
table = [n*i for i in range(1, 11)]
print(table)

with open ("Chapter-12 PS/1.txt","a")as f:
    f.write(str(table)+"\n")