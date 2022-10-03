def isomorphic(X,Y):
    if len(X)!=len(Y):
       return False
    d = {}
    s = set()
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
    if x in d:
        if d[X]!=y:
            return False
        else:
            if y in s:
                return False
            d[X] = y
            s.add
            return True
        if isomorphic(X,Y):
            print(f'{X} and {Y} are ismorphic')
        else:
            print(f'{X} and {Y} are not isomorphic')
            
