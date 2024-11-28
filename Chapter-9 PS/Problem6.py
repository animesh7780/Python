with open("Chapter-9 PS/log.html") as f:
    data = f.read()

if("python" in data):
    print("python is present")
else:
    print("python is not present")