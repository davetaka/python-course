weather_description = input("How is the weather? ")

is_hot = weather_description == "hot"
is_cold = weather_description == "cold"

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("it's a lovely day")

print("Enjoy your day")
