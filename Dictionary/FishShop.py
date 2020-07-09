# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:48:55 2020

@author: Aadhavan
"""

Fish_breeds = {
        2121:'Albino Tiger Oscar Cichlid',
        2122:'Black Molly',
        2123:'Yellow Guppy',
        2124:'Blue Mystery Snail',
        2125:'Tiger Oscar Cichlid',
        2126:'white Molly',
        2127:'blue Guppy',
        2128:'Yellow Mystery Snail',
        }
for Fish_codes in Fish_breeds :
    print("THESE ARE THE CODES:  ", Fish_codes, "    NAME OF THE FISH:  ", Fish_breeds[Fish_codes])

FishCode = int(input("ENTER THE CODE FOR THE FISH U WANT TO VIEW;  "))


counter=0
LIstOfCodes =[2121,2122,2123,2124,2125,2126,2126,2127,2128]
index = 0

if ( FishCode in Fish_breeds):
    print( Fish_breeds[FishCode] )
else:
    print("Given fish code is invalid")
#while FishCode != LIstOfCodes[index]:
#    print("TTT")
#    if FishCode == LIstOfCodes[index]:
#        print("gnhg")
#
#        counter += 1
#        if counter == 8:
#            print ("wrong code")
#    else:
#       print(Fish_breeds[FishCode])
#    index += 1