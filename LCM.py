def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Get user inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the LCM
lcm_result = lcm(num1, num2)
print(f"The LCM of {num1} and {num2} is: {lcm_result}")
