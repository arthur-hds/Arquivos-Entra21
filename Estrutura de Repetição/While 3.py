primo = 1
while primo <= 100:
    cont = 1
    div = 0
    while cont <= primo:
        if (primo / cont) == (primo // cont):
            div += 1
        cont += 1
        if div > 2:
            break
    if div == 2:
        print(f'{primo} é primo')
    primo += 1
