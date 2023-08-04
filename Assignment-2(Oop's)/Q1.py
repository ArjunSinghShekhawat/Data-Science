# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.

#Class-> class is a blueprint of an object and other words class is collections of objects like car,train.
#object ->object is a real world entity in which have state and behaviour is called object.

#class
class vehicle:
    def __init__(self,vehicle_name,max_spped,average_speed):
        self.vehicle_name = vehicle_name
        self.max_spped = max_spped
        self.average_speed = average_speed
#object
first = vehicle('toyata',120,60)
second = vehicle('inova',160,70)