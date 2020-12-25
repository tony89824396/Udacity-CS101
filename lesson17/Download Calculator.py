
def download_time(t,b,c,d):
    if b=="kb":
        b=2 ** 10
    elif b=="kB":
        b=2 ** 10 * 8
    elif b=="Mb":
        b=2 ** 20
    elif b=="MB":
        b=2 ** 20 * 8
    elif b=="Gb":
        b=2 ** 30
    elif b=="GB":
        b=2 ** 30 * 8
    elif b=="Tb":
        b=2 ** 40
    else:
        b=2 ** 40 * 8
    
    if d=="kb":
        d=2 ** 10
    elif d=="kB":
        d=2 ** 10 * 8
    elif d=="Mb":
        d=2 ** 20
    elif d=="MB":
        d=2 ** 20 * 8
    elif d=="Gb":
        d=2 ** 30
    elif d=="GB":
        d=2 ** 30 * 8
    elif d=="Tb":
        d=2 ** 40
    else:
        d=2 ** 40 * 8
        
    a=t*b*1.0/(c*d)
    sec=a%60.0
    min=int(a/60)
    r=min%60
    hr=int(min/60)
    if hr and  r and sec ==1:
        return str(hr)+" "+"hour" +","+" "+str(r)+" "+"minute" +","+" "+str(sec)+" "+"second"
    elif r and sec==1:
        return str(hr)+" "+"hours" +","+" "+ str(r)+" "+"minute" +","+" "+str(sec)+" "+"second"
    elif sec==1:
        return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"second"
    elif r==1:
        return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minute"+"," +" "+str(sec)+" "+"seconds"
    elif hr==1:
            return str(hr)+" "+"hour" +","+ " "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"seconds"
    else:
            return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"seconds"

