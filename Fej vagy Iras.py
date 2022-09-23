import random
randomszam = random.randint (1,2)
fejvagyiras = input ('Fej vagy Írás? ')
if fejvagyiras == 'Fej'and randomszam == 1:
    print ('Sikeresen eltaláltad hogy fej')
elif fejvagyiras == 'Írás'and randomszam == 2:
    print ('Sikeresen eltaláltad hogy Írás')
else:
    print('Nem talált')