
def symmetric(a):
    #1.[] 
    #2. 2-for loop-> Gen List-> Compare(if-else) 
    #3. len of whole list vs. len of list element(if-else)
    if a==[]:
        return True
        
    for i in range(0, len(a),1):
        if len(a) != len(a[i]):
            return False
    c=[]        
    for i in range(0, len(a),1):
        b=[]
        for j in range(0, len(a),1):
            b.append(a[j][i])
        c.append(b)
        print c
    if c==a:
        return True
    else:
        return False
    
    
    
    
    
