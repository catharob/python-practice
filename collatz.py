def collatz(number): #define collatz function
    if number%2 ==0:
        even = number//2
        print even
        return even #need both print and return. but why???
    else:
        odd = 3*number + 1
        print odd
        return odd
print 'Enter number:'


def continueCollatz(number): # repeat collatz function till reaches 1
    try:
        num = int(input())
        
        newNum = collatz(num)
        
        while newNum != 1:
            newNum = collatz(newNum)
            if newNum == 1:
                break
    except NameError: # returns error if a string is entered
        print "You must enter valid integer."
        continueCollatz(number)

continueCollatz(newNum)