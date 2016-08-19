'''
Write a function that prints out numbers to 100
but if that number is divisible by 3 instead of the number we print "Fizz"
if that number is divisible by 5 we print "Buzz"
and if that number is divisible by 5 and 3 we print "FizzBuzz"
'''
def function():
    for n in range(0,101):

        if (n % 5 ==0) and (n % 3 == 0):
            print ("Fizz")
        elif n % 5 ==0:
            print ("Buzz")
        
            print("FizzBuzz")
        else:
            print ("This is not divisible by 5 or 3")
