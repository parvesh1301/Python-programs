def reverse_num(n):
    reverse_num = 0
    while n != 0:
        digit =n % 10
        reverse_num = reverse_num * 10 + digit
        n = n // 10
    return reverse_num
n = int(input("Enter any digit number to reverse :"))
reverse = reverse_num(n)
print(f"The reverse of the {n} is :",reverse)