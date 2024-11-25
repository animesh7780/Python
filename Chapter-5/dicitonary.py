d ={} #empty dictionary

marks = {
    "Animesh": 90,
    "Chau": 90,
    "Dham Dham":12
}

marks["Animesh"] = 100

marks.update({"Dham Dham": 1235678, "Ernak": 123})
print(marks, type(marks))
print(marks["Dham Dham"])
print(marks.values())

print(marks.get("Animesh")) #if error returns none
print(marks["Animesh"]) #if error returms key error

