
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    i=year1
    a=0
    j=0
    list_j=[]
    list_month_leap=[31,29,31,30,31,30,31,31,30,31,30,31]
    list_month_common=[31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(year1,year2+1,1):
        if i%4 !=0:
            j=365
        elif i %100 !=0:
            j=366
        elif i%400 !=0:
            j=365
        else:
            j=366
        list_j.append(j)
    sum(list_j)
    if list_j[0]==365:
        month_year1=sum(list_month_common[0:month1-1])
    else:
        month_year1=sum(list_month_leap[0:month1-1])
    MD_1=month_year1+day1
    if list_j[-1]==365:
        month_year2=sum(list_month_common[month2:])
        day_diff=list_month_common[month2-1]-day2
    else:
        month_year2=sum(list_month_leap[month2:])
        day_diff=list_month_leap[month2-1]-day2
    MD_2=month_year2+day_diff
    answer=sum(list_j)-MD_1-MD_2
    return(answer)
    ##
    # Your code here.
    ##


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
