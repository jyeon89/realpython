def word_list():
    Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrover", "gorilla"]
    Verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    Adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    Prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "witin"]
    Adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    list = [Nouns, Verbs, Adjectives, Prepositions, Adverbs]

    return list

from random import randint
def makePoem():
    wl = word_list()

    N = 0
    V = 1
    Adj = 2
    P = 3
    Adv = 4

    noun1 = wl[N][randint(0,len(wl[N])-1)]
    wl[N].remove(noun1)
    noun2 = wl[N][randint(0,len(wl[N])-2)]
    wl[N].remove(noun2)
    noun3 = wl[N][randint(0,len(wl[N])-3)]
    wl[N].extend([noun1, noun2])

    verb1 = wl[V][randint(0,len(wl[V])-1)]
    wl[V].remove(verb1)
    verb2 = wl[V][randint(0,len(wl[V])-2)]
    wl[V].remove(verb2)
    verb3 = wl[V][randint(0,len(wl[V])-3)]
    wl[V].extend([verb1, verb2])

    adjective1 = wl[Adj][randint(0,len(wl[Adj])-1)]
    wl[Adj].remove(adjective1)
    adjective2 = wl[Adj][randint(0,len(wl[Adj])-2)]
    wl[Adj].remove(adjective2)
    adjective3 = wl[Adj][randint(0,len(wl[Adj])-3)]
    wl[Adj].extend([adjective1, adjective2])

    preposition1 = wl[P][randint(0,len(wl[P])-1)]
    wl[P].remove(preposition1)
    preposition2 = wl[P][randint(0,len(wl[P])-2)]
    wl[P].append(preposition1)

    adverb1 = wl[Adv][randint(0,len(wl[Adv])-1)]

    adj1 = adjective1[0]
    
    if adj1 == "a" or adj1=="e" or adj1=="i" or adj1=="o" or adj1=="u":
        A = "An"
        a = "an"
    else:
        A = "A"
        a = "a"
        
    print("{} {} {}".format(A, adjective1, noun1))
    print("{} {} {} {} {} the {} {}".format(A, adjective1, noun1, verb1, preposition1, adjective2, noun2))
    print("{} the {} {}".format(adverb1, noun1, verb2))
    print("the {} {} {} {} {} {}".format(noun2, verb3, preposition2, a, adjective3, noun3))
