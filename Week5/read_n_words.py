def read_n_word (fileName,number):
    number = number - 1
    fileName = open(fileName,"r")
    data = fileName.read()
    words = data.split() 
    number2 = number + 1
    number2 = number2
    return words[number]
    
pri = read_n_word("cities",5)
print(pri)