from __future__ import division
from random import randint

tail = 0
head = 0
tot = 0
count = 0
cnt = 0
sum = 0

for trial in range(1,10000):
    while randint(0,1) == 0:
        tail += 1
        #print(tail)
        head = 0
        cnt = 1
        count = 1
    
    head += 1

    tot += count + cnt
    sum += tail + head
    
    #print("        ", head, "     ", tot, "    sum: ", sum)
    count = 0
    cnt = 0
    tail = 0

avg = (sum/tot)

print("Avg: ~", avg, "tosses")
