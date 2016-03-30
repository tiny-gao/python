from sys import argv
script, filename = argv

txt = open(filename)
print txt.read()

answer = raw_input("you know the txt value?")

print "your answer is %r" % answer
