cars = 100

space_in_cars = 200

drivers = 30

passengers = 90

cars_not_driven = cars - drivers

cars_driven = drivers

carpool_activity = cars_driven * space_in_cars

average_passenger_per_car = passengers / cars_driven

print "There are", cars, "cars available"

print "There are only", drivers, "drivers available"

print "There will be", cars_not_driven, "empty cars today"

print "We can Transport", carpool_activity, "people today"

print "We have ", passengers, "to carpool today"

print "We need to put about", average_passenger_per_car, "in each car"


