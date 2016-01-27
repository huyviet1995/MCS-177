#int -> int
def presentsOnDay(day):
    """ Calculate the number of present offered by my true
    love in a particular day"""
    acc=0
    for i in range(day+1):
        acc+=i
    return (acc)

#int -> int         
def presentsThroughDay(lastDay):
    """ Calculate the number of presents added up until the last day"""
    acc=0
    for i in range(lastDay):
        acc+=presentsOnDay(i+1)
    return(acc)

#int -> int
def presentsOnDay(day):
    """ Calculate the number of presents on a specific day"""
    return day*(day+1)//2
