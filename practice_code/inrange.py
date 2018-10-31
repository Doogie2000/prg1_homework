def inrange(low_number, high_number, actual_number) :
    if (actual_number > low_number) and (actual_number < high_number):
            return True
    else : return False
number1 = 1
number10 = 10
number_in_range = 4
number_out_range = -4

isnumber1inrange = inrange(number1, number10, number_in_range)
print(isnumber1inrange)