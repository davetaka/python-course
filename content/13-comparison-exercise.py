name = input("what's your name? ")


if(len(name) < 3):
    print("the name must have at least three characters long")
elif(len(name) > 50):
    print("the name is too long, can be only a maximum fifty characters long")
else: 
    print("name looks good!")


