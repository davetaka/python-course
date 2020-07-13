birth_year = input('Birth year: ')
age = 2020 - int(birth_year)
print(age)

kg_weight = input('Weight: ')
print('your weight is: ' + kg_weight + 'kg')

lb_factor = 0.454
lb_weight = lb_factor * float(kg_weight)

print('your weight is: ' + str(lb_weight) + 'lb')
