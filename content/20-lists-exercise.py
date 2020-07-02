numbers = [10,5,20,25,22,40,30]

# try 1
print("\ntry 1")
numbers.sort()
print(f"largest number is {numbers[-1]}")

print("\ntry 2")
largestNumber = 0
for number in numbers:
    if largestNumber < number:
        largestNumber = number
print(f"largest number is {largestNumber}")