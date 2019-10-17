def search(uniqueLetters, letter):
    print( "Searching ", letter, " in ", uniqueLetters)
    count = len(uniqueLetters) - 1
    position = 0
    found = False;
    while(position <= count):
         
        if(letter == uniqueLetters[position]):
            found = True; 
        position += 1 
    return found

print( search("Hello", "7") )
        
word = input("PLEASE ENTER A WORD")
#position is greater
index = 1
position = len(word) - 1
uniqueLetters = []

found = False;
a=0
#if(True):
#    word[0].append(uniqueLetters[0]):
while (index <= position):
    print('e')
#    word[0].append(uniqueLetters[0])
    
    found = search( uniqueLetters, word[index] )
    if(found == False):
        uniqueLetters.append(word[index])
            
    index += 1
        
print (uniqueLetters)