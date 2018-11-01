def find_min_val(values) :
    new_val = values[0]
    for value in values :
        if new_val > value :
            new_val = value
    return new_val
def find_position(values, element):
    index = 0
    for value in values:
        if value == element:
            return index
        index += 1

def selection_sort(values):

    
    count = 0
    while (count < len(values)) :
        smallest_value = find_min_val(values[count: ])
        position = find_position (values,smallest_value)
        values[position] = values[count]
        values[count] = smallest_value
        count += 1
    return values

unsorted = [7,3,6,4,9,1,0,23,4,5,100]  
print(selection_sort(unsorted))    
    