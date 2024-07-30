def divisor (number):
    factor =[]
    for i in range ( 1 , number +1):
        if number % i == 0 :
            factor.append(i)
    return factor

num = int(input("Enter your number="))
print (f"The divisor of {num} are :{divisor(num)}")        