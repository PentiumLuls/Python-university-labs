#w1 = input ("1st word: ")
#w2 = input ("2nd word: ")
#w3 = input ("3rd word: ")

w1 = "as"
w2 = "adfg"
w3 = "adfth"

uniqueSymbols = []

for s in w1:
    if s not in uniqueSymbols and s not in w2 and s not in w3:
        uniqueSymbols.append(s)

for s in w2:
    if s not in uniqueSymbols and s not in w1 and s not in w3:
        uniqueSymbols.append(s)

for s in w3:
    if s not in uniqueSymbols and s not in w1 and s not in w2:
        uniqueSymbols.append(s)

print(uniqueSymbols)
