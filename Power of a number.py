def power (base,exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
    

base = int(input("Enter the base of the number :"))
exponent = int (input("Enter the exponent for your base number :"))

powerof = power (base,exponent)

print(f"The multiples of {base} power {exponent} is expected to be :",powerof)