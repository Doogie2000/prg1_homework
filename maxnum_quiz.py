#problem 1
raw_numbers = input ('''Input at least three numbers separated by a space
>>>''')
print('''These are your numbers
#########################
''' + raw_numbers)
cooked_numbers = raw_numbers.split(" ")
og_number = -1000000000000000000000000000000000
for number in cooked_numbers :
    if int(number) > og_number :
        og_number = int(number)
print ('''This is your highest number
##########################
'''
+ str(og_number))

