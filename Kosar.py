kosar1 = input ('Henrik megy ma kosarazni? (igen vagy nem) ')
kosar2 = input ('Hanna megy ma kosarazni? (igen vagy nem) ')
if kosar1 == 'igen' and kosar2 == 'igen': 
    print ('Mindketten jönnek kosarazni!')
elif kosar1 == 'igen' or kosar2 == 'igen':
    print ('Az egyikük biztosan megy kosarazni')
else:
    print ('Egyikük se megy kosarazni')
    