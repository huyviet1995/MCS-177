#Partner: Thao Le


import urllib.request;
#string,string,string -> boolean
def betweenDates(date1,date2,date3):
    '''take three date as inputs, return true if date1 between date2 and 3, including date2 but not date3,else return False'''
    date1=int(date1[0:4])*365+int(date1[5:7])*31+int(date1[8:10]);
    date2=int(date2[0:4])*365+int(date2[5:7])*31+int(date2[8:10]);
    date3=int(date3[0:4])*365+int(date3[5:7])*31+int(date3[8:10]);
    if (date1>=date2) and (date1<date3):
        return True;
    else:
        return False;

#string,string ->list of lists
def parseEarthquakeData(date2,date1):
    '''Take two dates as input, return a list of lists of Earthquake's data (latitude, longitude, depth and magnitude)
    that occured during the period between two days'''
    page=urllib.request.urlopen('http://www.choongsoo.info/teach/mcs177-sp12/projects/earthquake/earthquakeData-02-23-2012.txt');
    splitData=[]
    
    finalData=[];
    for aline in page:
        newLine=aline.decode('ascii');
        splitData=newLine.split(',');
        if (splitData[0]>=date2) and (splitData[0]<date1):
            if (len(splitData)!=6):
                newLine=aline.decode('ascii');
                splitData=newLine.split(',');
            else:
                finalData.append([float(i) for i in splitData[2:]]);
        if (splitData[0]<date2):
            break;
    return finalData

#float->string
def colorCode(depth):
    '''take a particular depth as input, return the color associated with it'''
    if (depth>=0) and (depth<=33):
        return 'orange';
    elif (depth<=70):
        return 'yellow';
    elif (depth<=150):
        return 'green';
    elif (depth<=300):
        return 'blue';
    elif (depth<=500):
        return 'purple';
    elif (depth<=900):
        return 'red';
    
import cTurtle;
myTurtle=cTurtle.Turtle();
#string,string ->void
def plotEarthquakeData(date1,date2):
    '''take two dates as input, plot all dots of different sizes and colors on a world map to represent particular Earthquakes during the period
    between two dates'''
    
    myTurtle.bgpic('worldmap.gif');
    myTurtle.setWorldCoordinates(-180,-90,180,90);
    myTurtle.speed(10);
    myTurtle.hideturtle();
    listData=parseEarthquakeData(date1,date2)
    for i in range(len(listData)):
        myTurtle.up();
        myTurtle.goto(listData[i][1],listData[i][0]);
        myTurtle.dot(4*listData[i][2],colorCode(listData[i][3]))

    
    
    
        
    


        
        
        
        
    

        
    
