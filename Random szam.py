import random
szam = random.randint (1,5)
igaz = True
while igaz:
    bekert_szam = input ('Adj meg egy számot! ')
    if int (bekert_szam) == int (szam):
        print('Eltaláltad a számot!')
        igaz = False
    elif int (bekert_szam) < int(szam):
        print('A megadott szám kisebb mint a random szám')
    else:
        print('A megadott szám nagyobb mint a random szám')
