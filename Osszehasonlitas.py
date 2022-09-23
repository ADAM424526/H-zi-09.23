import random
randomszam = random.randint (1,3)
bekertszam = int (input ('Adjon meg egy számot az összehasonlítás érdekében! '))
if randomszam == bekertszam:
    print ('A megadott számod és a random szám megegyezik')
elif randomszam > bekertszam:
    print ('A megadott szám kisebb mint a random szám')
else:
    print ('A megadott szám nagyobb mint a random szám')
