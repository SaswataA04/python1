class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        print("Type of Transport:", self.type)
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        print("Type of Transport:", self.type)
        print("Seat No:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


boat1 = Boat("Water", 50, "Kolkata", "Port Blair")
boat2 = Boat("Water", 80, "Mumbai", "Goa")

bus1 = Bus("Road", 25, "Delhi", "Agra")
bus2 = Bus("Road", 40, "Kolkata", "Durgapur")

print("Boat 1")
boat1.show()

print("\nBoat 2")
boat2.show()

print("\nBus 1")
bus1.show()

print("\nBus 2")
bus2.show()