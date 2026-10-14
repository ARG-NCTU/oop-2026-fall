class Vehicle:
    next_id = 1

    def __init__(self, plate, hours):
        self.plate = plate
        self.hours = hours
        self.vid = Vehicle.next_id
        Vehicle.next_id += 1

    def fee(self):
        return self.hours * 30

    def __str__(self):
        return f"#{self.vid} {self.plate}: {self.fee()}元"


class Motorcycle(Vehicle):
    def fee(self):
        return self.hours * 10


class Truck(Vehicle):
    def __init__(self, plate, hours, weight):
        Vehicle.__init__(self, plate, hours)
        self.weight = weight
    def fee(self):
        if self.weight > 10:
            return self.hours * 50 + 100
        else:
            return self.hours * 50


def total_fee(vehicles):
    total = 0
    for i in vehicles:
        total = total + i.fee()
    return total

if __name__ == "__main__":
    c = Vehicle("ABC-123", 2)
    m = Motorcycle("MOTO-1", 3)
    t = Truck("TRK-9", 2, 12)

    print(c)
    print(m)
    print(t)
    print(total_fee([c, m, t]))
