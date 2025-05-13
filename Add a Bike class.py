class Bike:
    def __init__(mybike, color, bike_type):
        mybike.color = color
        mybike.bike_type = bike_type
    
    def bike_info(bk):
        print(f"This is a {bk.color} {bk.bike_type}")
    
    def ride(bk):
        print(f"Riding the {bk.bike_type}")

# create bike object
my_bike = Bike("Black", "Mountain Bike")
my_bike.bike_info()
my_bike.ride()
