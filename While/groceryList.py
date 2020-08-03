Grocery = ["banana", "pineapple", "apple", "eggs", "coke" ]
letters = ("abc")
position = len(Grocery) - 1
index = 0
number = 0
word = ""
List = Grocery
for Groceries in Grocery :
    word =  Grocery[index]
    number = letters.find(word[0])
    if number >= 0 :
        Grocery.pop(index)
        position -= 1
        print(Grocery)
    else:
        print("no")
    index += 1
print(Grocery)