'''
How many times does a letter appear in a string?
How many times does a word appear in a sentence?
'''
word=input("enter a word > ")
letter_count = { }
for letter in word:
    if (letter in letter_count) :
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print (letter_count["t"])