numbers = [5, 2, 1, 7, 4]

numbers.append(13)
numbers.insert(0,13)
numbers.remove(5)

numbers.pop()

print(numbers)

if 1 in numbers:
    print(numbers.index(1))
    print("exists 1 in list")

print(50 in numbers)

if 50 in numbers:
    print("exists 50 in list")


print(numbers.count(2))
numbers.sort()
print(numbers)

numbers2 = numbers.copy()

numbers.clear()
print(numbers)