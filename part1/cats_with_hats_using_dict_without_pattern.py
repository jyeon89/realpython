from cats_with_hats_dict import cats_dict

def cats():
            
    cats = int(input("Number of Cats (0-100): "))
    laps = cats
    hats = []

    for lap in range(1, laps+1):
        for cat in range(1, cats+1):
            if cat%lap == 0:
                if cats_dict[cat] in hats:
                    hats.remove(cats_dict[cat])
                else:
                    hats.append(cats_dict[cat])

    print("Cat # with hats: ", hats)
