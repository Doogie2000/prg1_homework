#problem 1
print('''
Welcome to the bridge of Math 
Enter a number and be amazed 
vvvvvvvvvvvvvvvvvvvvvvvvvvvvv
''')

number_to_check = int(input("What is your favorite number? >>> "))
list_of_numbers = list(range(1,number_to_check))
factors = []
for x in list_of_numbers :
    y = number_to_check / x
    if (number_to_check % x == 0) :
        factors.append(x)
factors.append(number_to_check)
final_count = str(number_to_check) + (" has ") + (str(len(factors))) + (" factors, and those are ") + (str(factors))
print ('''
vvvv
''' +
final_count + ''' 
^^^^''')

#problem 2
