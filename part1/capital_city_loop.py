from capitals import capitals_dict
import random

def caploop():
        
    cd = capitals_dict
    loop = True

    while loop == True:
        state = random.choice(list(cd.keys()))

        cap = input("What is the capital of {}: ".format(state))

        if cap == cd[state]:
            print("Correct")
            out = input("Press any bottons to continue or type 'Exit' to exit: ")
        
            if out == "exit" or out == "Exit":
                loop = False
        else:
            print("Goodbye.")
            loop = False
        
    
