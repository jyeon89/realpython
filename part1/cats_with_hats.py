### I found a pattern that cats in number
### that can be perfectly squared rooted are the
### ones will be wearing a hat.

from cats_with_hats_dict import cats_dict
import math

def cats():
    num = input("Enter the number of cats (0-100): ") # input number of cats
    root = int(math.sqrt(int(num)))   # possible number of integers that can be squared
                            # in the range of total number of cats
    hats = []
    
    for i in range(1,root+1):
        hat_on = i**2
        hats.append(cats_dict[hat_on])
        
    print("List of cats wearing a hat: ")
    print(hats)

    
    
