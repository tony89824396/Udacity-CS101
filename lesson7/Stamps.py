print(2%2)
def stamps(a):
    d=int(a/5)
    b=int((a%5)/2)
    c=int((a%5)%2)
    return(d,b,c)
    # Your code here


print stamps(42)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
