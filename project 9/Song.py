#string->boolean
def checkWhiteSpace(string):
    '''check if a string contains only white space'''
    for letter in string:
        if letter!=' ':
            return True;
    return False;

class Song:
    #Song(string,string,string,string,string,string)
    def __init__(self,artist,album,song,mp3,genre):
        '''initialize all properties associated with the song'''
        self.artist=artist;
        self.album=album;
        self.song=song;
        self.mp3=mp3;
        self.genre=genre;

    #void->str
    def getArtist(self):
        '''get the name of the artist'''
        return self.artist;
    #void->str
    def getAlbum(self):
        '''get the name of the album'''
        return self.album;
    #void->str
    def getSong(self):
        '''get the name of the song'''
        return self.song;
    #void->str
    def getMp3(self):
        '''get the name of the file'''
        return self.mp3;
    #void->str
    def getGenre(self):
        '''get the name of genre'''
        return self.genre;
    #void->str
    def __str__(self):
        '''print the name, album and artist of a song in that order'''
        return self.song+' in '+self.album+' by '+self.artist;
    #str->void
    def setArtist(self,artist):
        '''set new name of the artist, return error if the new name only contains white space'''
        if checkWhiteSpace(artist): 
            self.artist=artist;
        else:
            print('please set artist name again');
    #str->void
    def setAlbum(self,album):
        '''set new name of the album, return error if the new name only contains white space'''
        if checkWhiteSpace(album):
            self.album=album;
        else:
            print ('please set album name again');
            
    #str->void
    def setSong(self,song):
        '''set new name of the song, return error if the new name only contains white space'''
        if checkWhiteSpace(song):
            self.song=song;
        else:
            print ('please set song name again');
            
    #str->void     
    def setMp3(self,mp3):
        '''set new name of the mp3 file, return error if the new name only contains white space'''
        if checkWhiteSpace(mp3):
            self.mp3=mp3;
        else:
            print ('please set mp3 name again');
    #str->void          
    def setGenre(self,genre):
        '''set new name of the mp3 file, return error if the new name only contains white space'''
        if checkWhiteSpace(genre):
            self.genre=genre;
        else:
            print ('please set genre name again');
