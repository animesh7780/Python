word = ["donkey", "bad ","money","sus"]

with open("Chapter-9 PS/censored.txt") as f:
    data = f.read()
    
for item in word:
    data = data.replace(item, "#"*len(item))
    
with open("Chapter-9 PS/censored.txt", "w") as f:
    f.write(data)
    