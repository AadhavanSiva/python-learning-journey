def uppercaseLowercase(word):
    lowerCaseLetters =  "abcdefghijklmnopqrstuvwxyz"
    upperCaseLetters =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = len(word) - 1
    index = 0
    values = [0,0]

    while index <= position:
        number = lowerCaseLetters.find(word[index])
        print ("hi")
        if number == -1  :
            print("e")
            number2 = upperCaseLetters.find(word[index])
            if number2 != -1 : 
                values[0] += 1
            else:
                 print("i")
        else :
            values[1] += 1
        index += 1
    return values
result = uppercaseLowercase("12345678")
print (result)