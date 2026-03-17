num = int(input("Enter num to check : "))
original = num
rev = 0
while num > 0:
    space = num % 10
    rev = rev * 10 + space
    num = num // 10

if original == rev:
    print("num is palindrome")
else:
    print("num is not palindrome")