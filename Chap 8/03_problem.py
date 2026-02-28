def sum(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + sum(n - 1)
n = int(input("Enter a number to find the sum of first n natural numbers: "))
result = sum(n)
print(f"The sum of first {n} natural numbers is {result}")