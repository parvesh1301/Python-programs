import math
def squarerootOf(number):
    if number <= 0 :
        print ("Please enter a valid number:")
    else:
        return math.sqrt(number)
num = int(input("Enter a number to check:"))
sqrtnum = squarerootOf(num)
print (f"The squareroot of {num} is:{sqrtnum} ")


