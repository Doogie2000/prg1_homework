print('''
Welcome to the bridge of Math 
''')

number_to_check = int(input("What is your favorite number? >>> "))
list_of_numbers = list(range(1,number_to_check))
factors = []
for x in list_of_numbers :
    y = number_to_check / x
    if (number_to_check % x == 0) :
        factors.append(y)

print(str(number_to_check) + " has " + str(len(factors) + "factors")
print (" and they are " + str(factors))