
def firstAndLastSame(text):
    position = len(text) - 1;
    if(text[position]== text[0]):
        return True;
    else:
        return False;

    
    
Word = input("Please enter a word")
same = firstAndLastSame(Word)

#index = 0;
#position = len(Word) - 1;
##print("hello")
#print(Word[0])
#print(Word[position])
#print(position)

if(same):
    print(" The sentence starts with and ends with ", Word[0])
else:
    print("The sentence does not start with and end with", Word[0])
