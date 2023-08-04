# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

class vehicle:
    def __init__(self,vehicle_name,max_spped,average_speed):
        self.vehicle_name = vehicle_name
        self.max_spped = max_spped
        self.average_speed = average_speed

class child(vehicle):
    def __init__(self,vehicle_name,max_spped,average_speed):
        super().__init__(vehicle_name,max_spped,average_speed)
        
    def seating_capacity(self,capacity):
        self.capacity = capacity
        return self.vehicle_name,self.capacity
    
obj = child('toyata',120,60)
print(obj.seating_capacity(5))

obj1 = child('inova',180,80)
print(obj1.seating_capacity(8))
    