date = str(input("Enter the date:"))
name = str(input(" name:"))

letter = '''
    Dear''',name,''',
    You are selected!
    ''',date
    
letter1 = '''
Dear name,
you are selected
date
'''

print(letter1.replace("name", name ).replace("date", date))
    
print(letter)
    
