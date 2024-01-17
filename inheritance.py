class vehicle:
    def general_usage(self):
        print("general usage: transportaion")

class car(vehicle):
    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Commute with family for vacation")


class motor_cycle(vehicle):
    def __init__(self):
        print("I am Motor-cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Road trip and racing")

c = car()
c.general_usage()
c.specific_usage()

m = motor_cycle()
m.general_usage()
m.specific_usage()

print(isinstance(c, vehicle))
print(isinstance(c, car))
print(isinstance(c, motor_cycle))

print(issubclass(car, vehicle))
print(issubclass(vehicle, car))
print(issubclass(motor_cycle, vehicle))
print(issubclass(car, motor_cycle))

