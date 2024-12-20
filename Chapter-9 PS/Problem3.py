import os

def generate_tables(n):
    
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    with open(f"tables/table-{n}.txt", 'w') as f:
        f.write(table)

for i in range(2, 21):
    generate_tables(i)
