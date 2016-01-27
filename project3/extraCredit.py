#string -> Integer
def strToInt(string):
    '''Take a string that contains only numbers and signs, return its integer
    value'''
    num=0
    bank='0123456789'
    cnt=1
    if (string[0]=='+'):
        stop=0
    elif (string[0]=='-'):
        stop=0
        cnt=-1
    else:
        stop=-1
        
    for i in range(len(string)-1,stop,-1):
        num+=bank.find(string[i])*cnt
        cnt=cnt*10
    return num
        
        
        
    
