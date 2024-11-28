f = open("Chapter-9 PS/poem.txt")
c = f.read()
if("twinkle" in c):
    print("Twinkle is present")
else:
    print("Twinkle is not present")
    
f.close()