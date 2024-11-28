word = "donkey"

with open("Chapter-9 PS/donkey.txt") as f:
    data = f.read()
    
datanew = data.replace(word, "####")

with open("Chapter-9 PS/donkey.txt", "w") as f:
    f.write(datanew)