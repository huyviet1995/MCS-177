#list,list->dict
def makeDictionary(list1,list2):
    '''take two list as input and match consecutive item in the first list to that in the second one to create a dictionary'''
    Dict={};
    for i in range(len(list1)):
        Dict[list1[i]]=list2[i]
    return Dict;

myIMDb={};
#string,list,list->void
def addMovie(title,characters,actors):
    '''add the title, a list of characters and a list of actors to the dictionary myIMDb'''
    movie={};
    for i in range(len(characters)):
        movie[characters[i]]=actors[i];
    myIMDb[title]=movie;
addMovie("Harry Potter and the Sorcerer's Stone",
        ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Albus Dumbledore'],
        ['Daniel Radcliffe', 'Emma Watson', 'Rupert Grint', 'Richard Harris'])
addMovie('The Hunger Games',
         ['Katness Everdeen','Primrose Everdeen','Gale Hawthorne','Effie Trinket'],
         ['Jennifer Lawrence','Willow Shields','Liam Hemsworth','Elizabeth Banks'])
addMovie('The Hobbits',
         ['Gandalf','Bilbo Baggins','Thorin','Balin'],
         ['Ian McKellen','Martin Freeman','Richard Armitage','Ken Stott'])
addMovie('Fifty Shades of Grey',
         ['Anastasia Steele','Christian Grey','Carla','Kate'],
         ['Dakota Johnson','Jamie Dornan','Jennifer Ehle','Eloise Mumford'])

#void->list
def listMovies():
    '''return all titles(keys) in the dictionary my IMDb'''
    return list(myIMDb.keys())

#string,string->string
def findActor(title,character):
    '''take title and character of the movie as input, return their associated actor. If there is no such title, print no such movie found'''
    if title not in myIMDb:
        print('No such movie found');
    elif character not in myIMDb[title]:
        print('No such character found');
    else:
        movie=myIMDb[title];
        return movie[character]

#string->void
def showCast(title):
    '''input the title of the movie, return a table characters and associated actors, if not such title is found, print out
    no such movie found'''
    if title in myIMDb:
        movie=myIMDb[title];
        print('Character            Actor/Actress',);
        print('------------------------------------',);
        Title=list(movie.keys())
        Title.sort()
        for key in Title:
            print(key.ljust(20),movie[key],);
    else:
        print('no such movie found');
        
        
        
        

    
        
        
