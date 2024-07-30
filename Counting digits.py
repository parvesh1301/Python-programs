def count_digits(n):
    if n == 0 :
        return 1
    count = 0
    while n != 0 :
        n = n // 10
        count += 1
    return count
n = int(input("Enter the number: "))
print(f"The number of digits of {n} are" , count_digits(n))

    