backwards_sentence=" "
sentence = "the quick brown fox jumped over the lazy dog"
words = sentence.split(" ")

for x in words :
    print (x)
    backwards = x [::-1]
    backwards_sentence = backwards_sentence + " "+backwards
print (backwards_sentence)

