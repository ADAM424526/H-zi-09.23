megadott_szam = int (input ('Adj meg egy egész számot: '))
if megadott_szam %3 == 0 and megadott_szam %4 == 0:
    print ('A megadott szám osztható hárommal és néggyel')
elif megadott_szam %3 == 0:
    print ('A megadott szám osztható hárommal')
elif megadott_szam %4 == 0:
    print ('A megadott szám osztható néggyel')
else:
    print ('A megadott szám nem osztható se néggyel se hárommal')


