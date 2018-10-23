
ask = int(input ("How many times would you like to count less than ten?"))


y = 0
while (y < ask) :
    x = 0
    stars = ""
    while (x < (ask)) :
        stars += "*  "
        #print("*  " * ask)
        x+=1
    print (stars) 

    y+=1

