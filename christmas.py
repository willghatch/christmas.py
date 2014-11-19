#!/usr/bin/env python

# In the spirit of Christmas joy, giving, and randomness, I present
# for your approval a program for randomizing the giving of gifts:

import random
import sys

allPeeps = sys.argv[1:]

if len(allPeeps) == 0:
    print("Usage: %s person1, person2, person3, ..."%sys.argv[0])
    sys.exit(0)

if len(allPeeps) == 1:
    print("Only one person?? You can't have a proper gift exchange alone!")
    sys.exit(1)

def pullFromHat(hat):
    "Pull a name out of the hat!"
    return hat.pop(random.randint(0,len(hat)-1))

def shuffleGifts():
    "Shuffle who gives to whom"
    peeps = list(allPeeps)
    whowhowho = {}
    for p in allPeeps:
        whowhowho[p] = pullFromHat(peeps)
        # if you draw your own name you have to redraw
        while whowhowho[p] == p:
            peeps.append(p)
            whowhowho[p] = pullFromHat(peeps)
    return whowhowho

result = shuffleGifts()

for peep in allPeeps:
    print("%s gives to %s"%(peep,result[peep]))

