def gcd (a,b):
    while b:
        
        a, b = b , a%b
        return a


num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))

gcd_result = gcd (num1 , num2)

print(f"the GCD of {num1} and {num2} is ",gcd_result)