customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])

# doesn't exists birthdate
print(customer.get("birthdate"))

# default value
print(customer.get("birthdate", "09/03/88"))

