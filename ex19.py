def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes" % boxes_of_crackers
    print "Mans that enough for a party"
    print "Get a Blanket. \n"

print "We can give the function numbers directly"
cheese_and_crackers(25, 10)

print "We can assign them to a variable"
amount_of_cheese = 25
amount_of_boxes = 15
cheese_and_crackers(amount_of_cheese, amount_of_boxes)

print "We can do math inside the arguement"
cheese_and_crackers(10+5, 20 -6)

print "We can assign then and Calculate"
cheese_and_crackers(amount_of_cheese+13, amount_of_boxes + 30)

