from sys import argv

script, filename = argv

print "We are going to erase %r" % filename
print "If you dont want to, then CTRL C"
print "If you do want it, then hit RETURN"

raw_input("?")

print "Opening the file..."

target = open(filename, 'w')

print "Truncating the file"
target.truncate()

print "Now i am going to ask you for three lines"

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Now i am going to write the file"

target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print "And we finally close it"
target.close()

print """
Types:
Read
Write
Close
Truncate
Readline
"""
