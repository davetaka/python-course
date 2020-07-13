house_price = 1000000
discount_percent = 0

credit_status = input("how is the buyer's credit status? ")

if credit_status == "good":
    discount_percent = 10
else:
    discount_percent = 20

print(
    f"the house's price for you is: {house_price - house_price*(discount_percent/100)}")
