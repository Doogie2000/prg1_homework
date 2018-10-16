raw_distance = input('''Please input your distances, separated by a space
>>>''')
print('''This is your distance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''' + raw_distance)
cooked_distance = raw_distance.split(" ")
og_distance = 
for distance in cooked_distance:
    if int(distance) > og_distance