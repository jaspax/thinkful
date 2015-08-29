max = 100
print "FizzBuzz counting to {0}".format(max)
for n in range(1, max):
    s = ""
    
    if n % 3 == 0:
        s += "Fizz"
    if n % 5 == 0:
        s += "Buzz"
    if s == "":
        s += str(n)
        
    print s