#string -> string
def unPigWord(word):
    """Take Pig Latin word as input, return the original word that is unpigged"""
    originalWord=""
    originalWord+=word[word.index('-')+1:len(word)-2]+word[0:word.index('-')]
    return originalWord

#string -> int
def findVowel(word):
    """ Take a word as input, return the position of the first vowel"""
    bank='aeiouAEIOU'
    for letter in word:
        if (letter in bank):
            return word.index(letter)
    return len(word)

#string -> string
def pigWord(word):
    """ Take a word as input, return is pig-latin form"""
    pig_word=""
    pig_word+=word[findVowel(word):len(word)]+'-'+word[0:findVowel(word)]+'ay'
    return pig_word

#string -> string
def unPig(strOfWords):
    '''Take a string of Pig Latin as input, unpig each individual word and return
    the whole unpigged string'''
    List=strOfWords.split()
    if (strOfWords==' '):
        return ' '
    for i in range(len(List)):
        List[i]=unPigWord(List[i])
    return ' '.join(List)

#string -> string
def pig(strOfWords):
    '''Take a string of words as input, return a string that contain Pig Latin version
    of each individual word'''
    List=strOfWords.split()
    if (strOfWords==' '):
        return ' '
    for i in range(len(List)):
        List[i]=pigWord(List[i])
    return ' '.join(List)




        


        
        
    
