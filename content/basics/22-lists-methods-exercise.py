numbers = [2, 2, 4, 6, 3, 4, 6, 1]
print(f"actual list: {numbers}")

# try 1
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(f"unique list: {unique_numbers}")

# try 2
unique_numbers = numbers.copy()

for number in numbers:
    while unique_numbers.count(number) > 1:
        unique_numbers.remove(number)

print(f"unique list: {unique_numbers}")
