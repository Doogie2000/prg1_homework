# Just Messing Around

name = input("Input animal please: ")

ans = input ("Are you sure you want to select " + name + "? ")
name = name.lower()
ans = ans.lower()
if ans == "yes" : print ("Ok!")
if ans != "yes" : name = input ("Please input a new name: ")
name = name.lower()
incorrect = ("Guess again!")
correct = ("It's listed!")
name_list = ["cat", "dog", "lion", "turtle", "bear", "frog", "alligator", "crocodile", "alpaca", "ant", "antelope", "ape", "armadillo", "donkey", "baboon", "badger", "bat", "bear", "beaver", "bee", "beetle", "buffalo", "butterfly", "camel", "carabao", "water buffalo", "caribou", "cattle", "cheetah", "chimpanzee", "chinchilla", "cicada", "clam", "cockroach", "fish", "coyote", "crab", "cricket", "crow", "deer", "dinosaur", "dolphin", "duck", "eel", "elephant", "elk", "ferret", "fly", "gerbil", "giraffe", "gnat", "goat", "wildebeest", "goldfish", "gorilla", "grasshopper", "guinea pig", "hamster", "hare", "bunny", "hedgehog", "herring", "hippo", "hornet", "hound", "hyena", "impala", "insect", "jackal", "jellyfish", "kangaroo", "wallaby", "koala", "leopard", "lizard", "llama", "locust", "louse", "macaw", "mallard", "mammoth", "manatee", "marten", "mink", "minnow", "mole", "monkey", "moose", "mouse", "rat", "mule", "muskrat", "otter", "ox", "oyster", "panda", "pig", "platypus", "porcupine", "prairie dog", "rabbit", "raccoon", "reindeer", "rhinoceros", "scorpion", "seal", "sea lion", "shark", "sheep", "skunk", "snail", "snake", "spider", "squirrel", "swan", "termite", "tiger", "tortoise", "walrus", "wasp", "weasel", "whale", "wolf", "wombat", "woodchuck", "groundhog", "worm", "yak", "yellow jacket", "zebra"]

for a_name in name_list :
    if name == a_name :
        name = "b"
       

if name!= "b" : print (incorrect)
if name == "b" : print (correct)       
    
