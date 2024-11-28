with open("Chapter-9 PS/log.html") as f:
    lines = f.readlines()
    lineno = 1
    for line in lines:
        
        if("python" in line):
            print(f"python is present: {lineno}")
            break
        lineno+=1
    else:
        print("python is not present")