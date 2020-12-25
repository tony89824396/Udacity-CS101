def convert_seconds(a):
    sec=a%60.0
    min=int(a/60)
    r=min%60
    hr=int(min/60)
    if hr and  r and sec ==1:
        return str(hr)+" "+"hour" +","+" "+str(r)+" "+"minute" +","+" "+str(int(sec))+" "+"second"
    elif r and sec==1:
        return str(hr)+" "+"hours" +","+" "+ str(r)+" "+"minute" +","+" "+str(sec)+" "+"second"
    elif sec==1:
        return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"second"
    elif r==1:
        return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minute"+"," +" "+str(sec)+" "+"seconds"
    elif hr==1:
        if sec%1==0:
            return str(hr)+" "+"hour" +","+ " "+str(r)+" "+"minutes"+"," +" "+ str(int(sec))+" "+"seconds"
        else:
            return str(hr)+" "+"hour" +","+ " "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"seconds"
    else:
        if sec%1==0:
            return str(hr)+" "+"hours" +","+" "+ str(r)+" "+"minutes"+"," +" "+ str(int(sec))+" "+"seconds"
        else:
            return str(hr)+" "+"hours" +","+" "+str(r)+" "+"minutes"+"," +" "+str(sec)+" "+"seconds"
        
    
    
