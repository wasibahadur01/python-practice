for i in range(100):
    if i==50:
        print("Breaking the loop at 50")
        break
    print(i)
    for i in range(100):
        if i==5:
            print("Breaking the inner loop at 5")
            continue
        print(i)