def decode_ellen_speak(string, count):
    string = list(string)
    if count > len(string) :
        return string
    elif count < len(string) and string[count] == string[count-1] and count > 0:
        string.remove(string[count-1])
        return decode_ellen_speak(string, count)
    else :
        return decode_ellen_speak(string, count + 1)


print(decode_ellen_speak("hhhhhoooowwww areeeee yyyooouuuuu", 0))
        
    