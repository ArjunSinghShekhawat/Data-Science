# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.
class vehicle:
    def __init__(self,vehicle_name,max_spped,average_speed):
        self.vehicle_name = vehicle_name
        self.max_spped = max_spped
        self.average_speed = average_speed
first = vehicle('toyata',120,60)
second = vehicle('inova',160,70)

print(first.vehicle_name)
print(first.average_speed)
print(first.max_spped)
