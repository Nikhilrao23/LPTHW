def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a + b

def subtract(a,b):
    print "Subtracting %d - %d" %(a,b)
    return a - b

def multiply(a,b):
    print "Multiplying %d * %d" %(a,b)
    return a * b

def divide(a,b):
    print "Dividing %d / %d" %(a,b)
    return a / b

print "Lets do some math with just functions"

age = add (30,5)
height = subtract(30,2)
weight = multiply(20,5)
iq = divide(40,4)

print "Age: %d, Height: %d, Weight: %d, iq: %d" %(age, height, weight, iq)

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That Becomes: ", what, "Can you do it by hand"
