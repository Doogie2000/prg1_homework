#Old Problem
''' def decode_ellen_speak(string, count):
    string = list(string)
    if count > len(string) :
        return string
    elif count < len(string) and string[count] == string[count-1] and count > 0:
        string.remove(string[count-1])
        return decode_ellen_speak(string, count)
    else :
        return decode_ellen_speak(string, count + 1) '''
#New Function
def whale_speak(message):
    if len(message) == 1 :
        return message
    elif message[0] != message[1] :
        return message[0] + whale_speak(message[1:])
    else:
        return whale_speak(message[1:])

print(whale_speak("hhhhhoooowwww areeeee yyyooouuuuu"))
        
    