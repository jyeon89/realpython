from random import random

countA1 = 0
countA2 = 0
countA3 = 0
countB = 0

for e in range(1,10000):
    if random() <= 0.87:
        countA1 = countA1 + 1
    if random() <= 0.65:
        countA2 = countA2 + 1
    if random() <= 0.17:
        countA3 = countA3 + 1

p1 = countA1/10000
p2 = countA2/10000
p3 = countA3/10000

win = (p1*p2*(1-p3) + p1*p3*(1-p2) + p2*p3*(1-p1) + p1*p2*p3) *100

print("{}% chance that A will win in Region 1".format(p1*100))
print("{}% chance that A will win in Region 2".format(p2*100))
print("{}% chance that A will win in Region 3".format(p3*100))
print("")
print("Chance that A will win the election: {}%".format(win))
