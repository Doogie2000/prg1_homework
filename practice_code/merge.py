def merge(items) :
    half = int(len(items)/2)
    items_left = items[:half]
    items_right = items[half:]
    if (len(items) == 1) :
        return items
    elif (len(items_right) > 1 ) :
        merge(items_right)
    elif (len(items_left) > 1 ) :
        merge(items_left)
    elif items_left > items_right :
        items_left = a
        items_left = items_right
        items_right = a
        return items_left, items_right 
merge([1,2,4,3,4])