#split input into list of integers
def seperate(items) :
    items_2 = []
    items = items.split(" ")
    for item in items :
        item = int(item)
        items_2.append(item)
    return items_2
#prob 1
def swap(a, b) :
    c = 0
    c = a
    a = b
    b = c
    return [a, b]

#prob 2
def bubble(items) :
    item_found = False
    index = 0
    while not item_found and (index < len(items)) :
        if index-1 >= 0 and items[(index)-1] > items[index]:
            swapped_items = swap(items[index-1], items[index])
            items[index-1] = swapped_items[0]
            items[index] = swapped_items[1]
        index += 1
    index = 1
    item_found = True
    while index < (len(items)-1) : 
        for item in items :
        
            if items[index] < items[index-1]:
                item_found = False
        index += 1
    return item_found

#prob 3
def bubble_sort(items) :
    sorted_list = bubble(items)
    while sorted_list == False :
        sorted_list = bubble(items)

b1 = input('''
input a list of numbers seperated by a space
>... ''')
b1 = seperate(b1)
bubble_sort(b1)
print(b1)