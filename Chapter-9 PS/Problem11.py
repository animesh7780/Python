with open("Chapter-9 PS/old.txt") as f:
    data = f.read()
    
with open("Chapter-9 PS/new.txt", "w") as f:
    f.write(data)