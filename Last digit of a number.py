def FindLastNum(number):
    number = abs(number)
    Last_digit = number % 10
    return Last_digit

number = int(input("Enter the number:"))

Last_digit = FindLastNum(number)
print(f"The last digit of {number} is {Last_digit}.")
