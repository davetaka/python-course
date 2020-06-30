print("guess a number between 0 and 9")

secret_number = 9
tries = 0
tries_limit = 3

# mine version
your_guess = None

while tries < tries_limit and your_guess != secret_number:
    your_guess = int(input("Guess: "))
    tries += 1

if(your_guess == secret_number):
    print("you won!")
else:
    print("sorry you failed!")
    quit()

# course version
print("guess again, round 2")
tries = 0
your_guess = None
secret_number = 8

while tries < tries_limit:
    your_guess = int(input("Guess: "))
    tries += 1
    if(your_guess == secret_number):
        print("you won!")
        break
else:
    print("sorry you failed!")