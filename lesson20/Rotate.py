def rotate(x,n):
    if n>=0:
        ans=""
        for i in range(0,len(x)):
            a=n%26
            b=x[i]
            c=ord(x[i])+a
            if ord(b)!=32 and c>(97+25):
                c=c-(26)
                d=chr(c)
                ans=ans+d
            elif ord(b)==32:
                ans=ans+" "
            else:
                d=chr(c)
                ans=ans+d
    else:
        ans=""
        for i in range(0,len(x)):
            a=(n*-1)%26
            b=x[i]
            c=ord(x[i])-a
            if ord(b)!=32 and c <97:
                c=97+(c-97+26)
                d=chr(c)
                ans=ans+d
            elif ord(b)==32:
                ans=ans+" "
            else:
                d=chr(c)
                ans=ans+d
    return ans 
    
