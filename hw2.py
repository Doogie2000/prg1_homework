
# problem 1

attendees = input("How many people will be joining us tonight? ")
if attendees == "1" : 
# extra credit?
    at2 = input("Just you then? Are you sure? ")
    at2.lower()
    if at2 == "yes" : 
        print("Sorry ")
    if at2 != "no" : 
        print("Lies!") 
    else : 
        print("What?")
elif attendees == "2" : 
    print("Bring marshmellows, please. ")
elif attendees >= "3" and attendees < "6" : 
    print("More than three is a croud amigo. ")
elif attendees >= "7" : 
    print("Party! ;) ")
else : 
    print("What dimension have you entered? ")




# problem 2

speed_limit = int(input("What was the speed limit? "))
speed_actual = int(input("How fast were you actually going? "))
b_day = input("Is it your birthday today? ")
b_day =b_day.lower()
if b_day == "yes" : 
    name = input("Then what is your name? ")
if b_day == "yes" : 
    speed_actual = speed_actual - 5
if b_day == "yes" : 
    print ("Happy birthday to you, Happy birthday to you, Happy birthday dear " + name + " Happy birthday to you!")
if speed_actual <= speed_limit : ticket = "No Ticket For You!"
elif speed_actual <= (speed_limit + 5) : 
    ticket = "You get a warning"
elif speed_actual < (speed_limit + 15) : 
    ticket = "You get a small ticket"
elif speed_actual == (speed_limit * 2) :
    ticket = "You get a license suspension"
elif speed_actual > (speed_limit + 15) : 
    ticket = "You get a big ticket"


print (ticket)
