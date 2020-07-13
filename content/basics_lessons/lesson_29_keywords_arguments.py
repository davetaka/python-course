def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")

your_name = input("your name is: ")
your_surname = input("your last name is: ")
greet_user(last_name=your_surname, first_name=your_name)

print("Finish")
