#!/usr/bin/env python
# $ ./cash
# Change owed: 0.41
# 4

def decimals(value):
     before, after = str(value).split(".")
     if len(after) == 0:
         return 1
     return 10**len(after)
     
while True:
    value = input("Value: ")
    if value <= 0:
        continue

    value = int(value * decimals(value))
    print(value)
    
    coin = [25, 10, 5, 1]
    nUniqueCoins = 0
    nCoins = 0
    change = []

    for c in coin:
        while value % c != value:
            nUniqueCoins = nUniqueCoins + 1
            nCoins = nCoins + value/c
            value = value % c
            change.append(c)

    print(nUniqueCoins, nCoins, change)
    break
