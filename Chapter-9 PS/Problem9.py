with open("Chapter-9 PS/this.txt") as f:
    data = f.read()
    
with open("Chapter-9 PS/copy_this.txt") as f:
    data1 = f.read()
    
if(data == data1):
    print("Same")
else:
    print("Not Same")