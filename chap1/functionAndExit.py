from sys import exit

def a():
   print "a"
def b():
   print "b"
def exit_0():
   exit(0)
def start():
   input = raw_input("> ")
   if input == "a":
        a()
   elif input == "b" :
        b()
   else :
        exit_0()

start()
