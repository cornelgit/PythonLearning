people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

# sorting function - to sort by name
# def f(person):
#     return person["name"]

# but we can use a condensed lambda function -> include the function as a single value on a single line

people.sort(key=lambda person: person["name"])

print(people)