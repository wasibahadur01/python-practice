def parttern(n):
    if (n == 0):
        return
    print("*" * n)
    parttern(n - 1)

parttern(5)


