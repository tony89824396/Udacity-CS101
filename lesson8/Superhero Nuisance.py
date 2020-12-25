def fix_machine(debris, product):
    n=0
    while n<len(product):
        a=debris.find(product[n])
        if a==-1:
            return("Give me something that's not useless next time.")
            
        n=n+1
        
    return product
        
