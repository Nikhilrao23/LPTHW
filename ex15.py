from sys import argv

script, filename = argv

txt = open(filename)


print "This is your filename %r" % filename
print txt.read()

print "Type your filename again"
file_again = raw_input("> ")

type_again = open(file_again)

print type_again.read()


