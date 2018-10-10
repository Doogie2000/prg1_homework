'''
a strong number is defined as a number that has the sum of the factorial of each
digit is equal to its original number
'''
print("please input a number that might be strong")
snumber = input(">> ")
digits = list(snumber)
sum = []
for digit in digits :
    factorial = 1
    for number in range (1, int(digit)+1) : 
        factorial = number * factorial
    sum.append(factorial)
    print(factorial)
final_factorial = 0
for number in sum :
    final_factorial += number
final_factorial = str(final_factorial)
if final_factorial == snumber :
    print (snumber + " is a strong number")
else : print(snumber + " is not a strong number")


    