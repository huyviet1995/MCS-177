import random;

#str->boolean
def checkWhiteSpace(string):
    '''check if a string only contains white spaces'''
    for letter in string:
        if letter!=' ':
            return True;
    return False;

class Playlist:
    #Playlist(str,listOfObjects,boolean)
    def __init__(self,name,songs,playStatus):
        '''initialize properties associated with a list'''
        self.name=name;
        self.songs=songs;
        self.random=playStatus;
        self.played=[];
        self.cnt=0;

    #void->str
    def getName(self):
        '''get the name of the playlist'''
        return self.name;
    #void->str
    def getSongs(self):
        '''get the list of songs of the playlist'''
        return self.songs;
    #void->str
    def getPlayStatus(self):
        '''get the play order, check songs are played in order or not'''
        return self.random;
    #str->void
    def setName(self,name):
        '''set new name of the playlist, return error if the new name only contains only white spaces'''
        if name==' ':
            print ('please set new name again')
        else:
            self.name=name;   
    #str->void        
    def setSong(self,newSong):
        '''set new list of songs, return error if the new list only contains only white spaces'''
        for song in newSong:
            if not checkWhiteSpace(str(song)):
                print('set new song again');
        self.songs=newSong[:];

    #str->void    
    def setRandom(self,playStatus):
        '''set new play status of the song, return error if the new status only contains white spaces'''
        if checkWhiteSpace(str(playStatus)):
            self.random=playStatus;
        else:
            print('please set play status again');

    #str->void
    def addSong(self,newSong):
        '''add new song to the list of songs, return error if the new list only contains spaces'''
        if checkWhiteSpace(str(newSong)):
            self.songs.append(newSong)
        else:
            print('add new song again')
    #void->str
    def __str__(self):
        '''print each song(title,album,artist) in the list of songs'''
        printList="PlayList: "+self.name;
        for song in self.songs:
            printList+='\n'+str(song);
        return printList;
    #void->str
    def nextSong(self):
        '''play next song in order if the random status is false, shuffle the song if the status is true'''
        if (self.random==False):
            playedSong=self.songs[self.cnt]
            self.cnt+=1;
            if (self.cnt>=len(self.songs)):
            
                self.cnt=0
                
            return str(playedSong)
        else:
            
            playedSong=random.choice(self.songs);
            while playedSong in self.played:
                playedSong=random.choice(self.songs);
            self.played.append(playedSong);    
            if len(self.played)==len(self.songs):
                self.played=[];
            return str(playedSong)

        
            
                
            
            
             
                 
                 
            
        
        
            
        
    
        
        
    
    
        
    
            
