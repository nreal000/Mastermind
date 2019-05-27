import random

keywords = "1 2 3 4 5 6".split()
value = random.choices(keywords,k=4)
print(value)
for i in range(1,2):
    guess = input("Guess 4 numbers from 1-6 spaced out: ").split()
    guess = "1 2 1 1".split()
    #copies both lists
    gue = guess.copy()
    val = value.copy()
    out = ""#output
    match = []
    for i in range(0,4):
        if value[i] == guess[i]:
            match.append(i)
            out += "+"
    for i in match[::-1]:
        del gue[i]
        del val[i]
    del match
    for j in gue:
        if j in val:
            out += "-"
            val.remove(j)
    del gue
    del val
    print(out)
