lst = [5, 2, 8, 1, 9]
largest = 0
second_largest = 0
for num in lst:
    largest = max(lst)
    if num < largest and num > second_largest:
        second_largest = num
print(second_largest)