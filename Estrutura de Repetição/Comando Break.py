cont = 1
tot = 0
while True:
    tot = 2**cont
    print(tot)
    cont += 1
    if tot > 30000:
        break