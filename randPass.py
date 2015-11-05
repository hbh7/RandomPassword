# Programmer: Matthew Griffin
#
# Importing stuff
try:
    import random
    import sys
    import string
    import datetime
    
except ImportError:
    print("Python" + str(sys.version) + "is not installed correctly.")

class Password:
    def __init__(self):
        print(datetime.date.today())
        print("GENERATING RANDOM PASSWORD...")
        
        for x in range(0, 2000):
            randNum = random.randint(0, 9)
            randLetter = random.choice(string.ascii_letters) # string.ascii_letters contains all letters
            
            print(str(randNum) + str(randLetter), end="")

if(__name__ == "__main__"):
    password = Password() 

