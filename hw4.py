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
word_real = []
phonetic_alpha=[]
print("Please type out a word")
word_real = input(">>>")
print (word_real)
word = list(word_real)
for letter in word :
    letter = letter.lower()
    for letter in word :
        if (letter == "a") :
            phonetic_alpha.append("alpha")
        elif (letter == "b") :
            phonetic_alpha.append("bravo")
        elif (letter == "c") :
            phonetic_alpha.append("charlie")
        elif (letter == "d") :
            phonetic_alpha.append ("delta")
        elif (letter == "e") :
            phonetic_alpha.append("echo")
        elif (letter == "f") :
            phonetic_alpha.append ("foxtrot")
        elif (letter == "g") :
            phonetic_alpha.append ("golf")
        elif (letter == "h") :
            phonetic_alpha.append ("hotel")
        elif (letter == "i") :
            phonetic_alpha.append ("india")
        elif (letter == "j") :
            phonetic_alpha.append ("juliet")
        elif (letter == "k") :
            phonetic_alpha.append ("kilo")
        elif (letter == "l") :
            phonetic_alpha.append ("lima")
        elif (letter == "m") :
            phonetic_alpha.append ("mike")
        elif (letter == "n") :
            phonetic_alpha.append ("november")
        elif (letter == "o") :
            phonetic_alpha.append ("oscar")
        elif (letter == "p") :
            phonetic_alpha.append ("papa")
        elif (letter == "q") :
            phonetic_alpha.append ("quebec")
        elif (letter == "r") :
            phonetic_alpha.append ("romeo")
        elif (letter == "s") :
            phonetic_alpha.append ("sierra")
        elif (letter == "t") :
            phonetic_alpha.append ("tango")
        elif (letter == "u") :
            phonetic_alpha.append ("uniform")
        elif (letter == "v") :
            phonetic_alpha.append ("victor")
        elif (letter == "w") :
            phonetic_alpha.append ("whiskey")
        elif (letter == "x") :
            phonetic_alpha.append ("x-ray")
        elif (letter == "y") :
            phonetic_alpha.append ("yankee")
        elif (letter == "z") :
            phonetic_alpha.append ("zulu")
        else : print ("Letter does not register as letter")
    break 

print( '''
~~~~~~~~~~~~~~~~~
''' + word_real + " is the answer you gave " + '''
~~~~~~~~~~~~~~~~~ 
''' +
str(phonetic_alpha) + " is the phonetic answer" + '''
~~~~~~~~~~~~~~~~~ '''
)