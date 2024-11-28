with open("Chapter-9 PS/this.txt") as f:
    data = f.read()

with open("Chapter-9 PS/copy_this.txt", "w") as f:
    data = f.write(data)