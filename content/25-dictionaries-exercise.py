phone = input("please inform your phone number: ")

spelled_numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

for number in phone:
    if not spelled_numbers.get(number) == None:
        print(f"{spelled_numbers[number]}", end = " ")

print()


# solution
output = ""

for ch in phone:
    output += spelled_numbers.get(ch, "!") + " "

print(output)


# best solution for me
output = ""
for number in phone:
    output += spelled_numbers.get(number, number) + " "

print(output)