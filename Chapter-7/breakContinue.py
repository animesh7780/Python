#breaks the value after the value is reached
for i in range(100):
    if i == 5:
        break
    print(i)

#skips the encountered value
for i in range(0,101, 2):
    if i == 34:
        continue
    print(i)