numbers = [5,2,5,2,2]

# try 1
print("\ntry 1")
for number in numbers:
    line = ""
    for x in range(number):
        line += "x"

    print(line)

print("\ntry 2")
# try 2 cheating
for number in numbers:
    print("x" * number)


# try 3
print("\ntry 3")
for number in numbers:
    for x in range(number):
        print("x", end = "")
        
    print()