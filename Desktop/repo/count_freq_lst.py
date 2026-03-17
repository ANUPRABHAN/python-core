li = ["hi", "hello", "HRU", "WRY", "bye","hi"]
target = str(input("Please enter word : "))
count = 0
for x in li:
    if x == target:
        count += 1
print(count)