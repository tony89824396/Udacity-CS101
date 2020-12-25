def is_identity_matrix(a):
    #check length nxn 
    for i in range(0,len(a)):
        if not len(a[i])==len(a):
            return False
    #diagonal has value
    for i in range(0, len(a)):
        if not a[i][i]==1:
            return False
    #check other row/column value==0
    store=[]
    for i in range(0, len(a)):
        temp=[]
        for j in range(0, len(a)):
            temp.append(a[i][j]*0)
        store.append(temp)
    for i in range(0, len(a)):
        store[i][i]=1
    if store==a:
        return True
    else:
        return False
