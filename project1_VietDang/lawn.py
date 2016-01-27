def timeToMow(depth,width):
     return depth*width/2/3600

def roundedTimeToMow(depth):
     return round(timeToMow(depth,16/9*depth))

i=100;
print ('depth',"   ",'roundedTimeToMow')     
for i in range(100,200,10):
     print (i,'    ',roundedTimeToMow(i))
     
     
     
          
     
     
          

          
          


