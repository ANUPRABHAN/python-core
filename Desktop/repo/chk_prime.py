num = int(input("Enter a number : "))
if num < 2:
    print("it's not a prime")
else:
    for i in range(2,num):
        if num % i == 0:
            print("it's not a prime")
            break
    else:
        print("it's prime")