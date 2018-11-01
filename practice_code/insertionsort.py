def find_min_val(values) :
    new_val = values[0]
    for value in values :
        if new_val > value :
            new_val = value
    return new_val

def insertion_sort(values):
    inorder = []
    while len(values) > 0 :
        smallest = find_min_val(values)
        values.remove(smallest)
        inorder.append(smallest)
    return inorder
        
unsorted = [1,5,23,6,0,86.2,3,6,1,0]

print(insertion_sort(unsorted))