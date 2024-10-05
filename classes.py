#  Class definition
# init is like a constructor, self is like this
class Point():
    def __init__(self, xInput, yInput):
        self.x = xInput
        self.y = yInput


p = Point(2, 8)
print(p.x)
print(p.y)



class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)


people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    result = flight.add_passenger(person)
    if result:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

