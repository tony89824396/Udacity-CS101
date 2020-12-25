

def biggest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    elif c>=a and c>=b:
        return c
    else:
        return "no biggest"
        
def set_range(a,b,c):
    big=biggest(a,b,c)
    range=biggest(big-a,big-b,big-c)
    return range
    
    
    
    # Your code here


print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6
