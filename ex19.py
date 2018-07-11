def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes!" % boxes_of_crackers
    print "Men That's enough for the party"
    print "Get a Blanket\n."


print "We can give them direclty"
cheese_and_crackers(23, 50)

print "Or We can give variables"
amount_of_cheese = 10
amount_of_boxes = 15

cheese_and_crackers(amount_of_cheese, amount_of_boxes)

print "We can do the math inside of this"
cheese_and_crackers(10+5, 20-10)

print "We can combine both of them together"
cheese_and_crackers(amount_of_cheese+100, amount_of_boxes+150)

