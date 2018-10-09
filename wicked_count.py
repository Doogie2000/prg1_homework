score = []
score = input("Please Enter Five Numbers With a Space In Between")
score = score.split(" ")

real_count = []
sum = 0
for x in score :
    score_1 = int(x)
    real_count.append(score_1)
    sum += score_1
print(sum)
print("This is not your count")

score = 0
for wicked in real_count :
    wicked = float(wicked)
    if (wicked == 13.0) :
        score += -100
    elif (wicked == 7) :
        score += 30
    elif (wicked %2 == 1) :
        score += wicked * 2
    elif (wicked %2) == 0 :
        score += wicked/2
    else : print("Not valid")
print (score)
print( '''
^^^^^^^^^^^^^^^^^^^^^^
This is your wicked score
''' )
