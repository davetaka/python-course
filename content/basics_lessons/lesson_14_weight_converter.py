weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").upper()

if(unit != "L" and unit != "K"):
    print("you have informed a wrong unit, the unit must be an L or a K")
    quit()

converted_weight = 0
converted_unit = ""
lb_to_kg_factor = 0.454

if(unit == "L"):
    converted_weight = weight * lb_to_kg_factor
    converted_unit = "kg"
else:
    converted_weight = weight / lb_to_kg_factor
    converted_unit = "lb"

print(f"Your converted weight is: {converted_weight} {converted_unit}")