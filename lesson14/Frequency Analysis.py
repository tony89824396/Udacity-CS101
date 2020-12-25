
def freq_analysis(a):
    count=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(0,len(a)):
        number=ord(a[i])-97
        count[number]=count[number]+1
    
    for i in range(0,26):
        count[i]=count[i]*1.0/len(a)
        
    return count
       
