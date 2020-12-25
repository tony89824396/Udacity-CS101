
def print_abacus(value):
    n=9
    for i in range(1,13,1):
        if n<0:
            break
        diff=int(value/10**n)
        value=value-(10**n)*int(value/10**n)
        n=n-1
        if diff==0:
            print("|00000*****   |")
        elif diff==1:
            print("|00000****   *|")
        elif diff==2:
            print("|00000***   **|")
        elif diff==3:
            print("|00000**   ***|")
        elif diff==4:
            print("|00000*   ****|")
        elif diff==5:
            print("|00000   *****|")
        elif diff==6:
            print("|0000   0*****|")
        elif diff==7:
            print("|000   00*****|")
        elif diff==8:
            print("|00   000*****|")
        elif diff==9:
               print("|0   0000*****|")
        else:
            break
