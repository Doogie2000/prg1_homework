raw_distance = input('''Please input your distances, separated by a space
>>>''')
print('''These are your distances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' + raw_distance)
cooked_distance = raw_distance.split(" ")

og_distance = 0
for distance in cooked_distance:
    og_distance = int(distance) - og_distance
    if int(distance) > og_distance :
        greatest_distance = int(distance)


print (greatest_distance)
#not the solution, but as close as I can get within time    