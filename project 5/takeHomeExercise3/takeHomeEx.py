def init():
    a=[];
    data=open('takeHomeEx.txt','r');
    n=int(data.readline());
    for i in range(n):
        a.append([]);
        a[i]=int(data.readline());
        
        
    data.close();

    output=open('output.txt','w');
    acc=sum(a);
    output.write(str(acc));
    output.close();



