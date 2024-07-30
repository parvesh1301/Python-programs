def arm_num(number):
    string_arm = str(number)
    num_arm = len(string_arm)

    sum_of_numbers = sum (int(digit)**num_arm for digit in string_arm  )
    return sum_of_numbers == number
num = int (input ("Enter your number:"))

if arm_num(num):
    print(f"The number{num} is an armstrong number")
else:
    print(f"The number {num} is not an armstrong number")
