'''
def count_up(count = 0, range = 10):
    if (count > range):
        return 
    else : 
        print(count)
        return count_up(count + 1)
    
count_up(0,range = int(input("What would you like to count up to? > ")))



def count_down(count = 10):
    if (count >= 0):
        print(count)
        return count_down(count - 1)
    else :
        return

count_down(int(input("What would you like to count down from? > ")))

def simple_bunny_count(bunnies):
    if bunnies == 0 :
        return 0
    else : 
        return 2 + simple_bunny_count(bunnies - 1)
print(simple_bunny_count(int(input("How many bunnies are there? "))))
'''
def complex_bunny_count(bunnies):
    if bunnies == 0 :
        return 0 
    elif (bunnies %2 == 0) :
        return 2 + complex_bunny_count(bunnies - 1)
    else :
        return 3 + complex_bunny_count(bunnies - 1)

print(complex_bunny_count(int(input("How many bunnies are there? "))))