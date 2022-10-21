from pydoc import importfile
from random import randint
from os import system

# will generate word and make the user guess the letters of that word
#The user only knows how many letters in the word
system('clear')
dictionary = ['stream', 'programming', 'title', 'moon','fishhook', 'night', 'python' , 'javascript', 'table']
# Random pick from a list
pic_a_word = dictionary[randint(0, len(dictionary)-1)]
list_pic_word = list(pic_a_word)
# counter for the while loop
i=0
#Display of the missing and found letters
display_mock = ' '.join([ "_" for elem in pic_a_word])
# Length of the picked word and found are the number of the letters found
n = len(list_pic_word)
found = 0
print('There is a hidden word below guess the letter of the word')
print('The right letters will reveal your word==>  ',display_mock )


while i<7:
    i=i+1
    letter_input = input('Which letter you think is in the word?    ').lower()
    # reset the index count for the hidden word when new letter guessed
    index= 0
    new_letter=[]
    for j in list_pic_word:
        
        if letter_input == j:
            found = found + 1
            # reset the count by one since it was a right guess
            i= i-1
            new_letter = list(display_mock)
            new_letter[index] = j
            display_mock = ''.join([ str(elem) for elem in new_letter])
        # else:
        #     print("This letter is not in the word") 
        index = index+2
        
    
    if (found < n) and (i < 7):
        print('You may only miss ', 7-i, " times")
        print("This how many letters you got =>",display_mock.upper()) 
        continue
    elif i== 7:
        print("You loose the word was ", pic_a_word.upper())
        break
    else:
        print ("You Win Great work!  The word was", pic_a_word.upper())
       
        break
           

    
