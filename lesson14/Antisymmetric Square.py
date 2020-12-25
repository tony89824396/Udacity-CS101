def antisymmetric(a):
    compare1=[]
    compare2=[]
    # [] null is True
    if a==[]:
        return True
    # check if it's nxn square or not.
    if not len(a)==len(a[0]):
        return False
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(a)):
            b=a[i][j]
            temp.append(b)
        compare1.append(temp)

        
    for i in range(0,len(a),1):
        temp2=[]
        for j in range(0,len(a),1):
            c=-1*a[j][i]
            temp2.append(c)
        compare2.append(temp2)

            
    if compare1==compare2:
        return True
    else:
        return False
    
