from sys import argv
script, filename = argv

print "file name is : %s" % filename
target = open(filename, 'w')
text = raw_input("input to the file : ")
target.write(text)
target.truncate()
target.close()
