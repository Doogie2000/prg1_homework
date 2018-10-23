nicknames = {
"douglas" : "doogie", 
"Mr. Stadler" : "dj shakes", 
}

nicknames ["yoon"] = "groot"
nicknames ["backus"] = "buckus"
nicknames ["crosby"] = "crispy"

final_string = ""

for name in nicknames :

    final_string += (name + " goes by the name " + nicknames[name] + ": ")

print(final_string)