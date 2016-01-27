def presentsOnDay(day):
    acc=0
    for i in range(day+1):
        acc+=i
    return (acc)
        
def presentsThroughDay(lastDay):
    acc=0
    for i in range(lastDay):
        acc+=presentsOnDay(i+1)
    return(acc)

##def presentsOnDay(day):
##    return day*(day+1)//2
