
def numbers_in_lists(a):
    a=a[::-1] #66232 1235554
    b=int(a) 
    prev=0
    ans=[]
    temp=[]
    current= int(b%10) #5
    while current>0:
        if prev >= current:
            temp.append(current)
        else:
            if not temp==[]:
                ans.append(temp)
                temp=[]
            ans.append(current)
            prev=current
        b=int(b/10)
        current=int(b%10) #2
    
    if not temp==[]:
        ans.append(temp)
    print ans
    return ans
    
    
