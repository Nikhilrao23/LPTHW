print "You enter a dark room with two doors. Do you go through door#1 or door#2"

door = raw_input(">")

if door == "1":
    print "There is a giant bear here eating a cheese cake. What do yo do?"
    print "1. Take the cake?"
    print "2. Scream at the bear"

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats off your face off. Good Job!"
    elif bear == "2":
        print "The bear eats off your leg off. Good Job!"
    else:
        print "Well, doing %s is probably better. Bears run away" % bear


elif door == "2":
    print "You Stare at the endlesss abyss at chultutu's retina"
    print "1. Blueberries"
    print "2. Yellow Jacket clothesspin"
    print "3. Understanding revovlers  yelling melodies"

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your Body survives powered by a mind of jello. Good Job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good Job!"

else:
    print "You Stumble around and fall on a knife and die. Good job"



