# available commands help, start, stop, quit

print("Welcome to course's car game:")

command = None
car_on = False

while command != "quit":
    command = input(">").lower().strip()

    if command == "help":
        print("start = starts the car")
        print("stop = stops the car")
        print("quit = quits the program")
    elif command == "start":
        if not car_on:
            print("Car started... ready to go")
        else:
            print("Car already started")

        car_on = True
    elif command == "stop":
        if car_on:
            print("Car stopped!")
        else:
            print("Car already stopped")

        car_on = False
    elif command != "quit":
        print("i don't understand that")
