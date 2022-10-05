letters= ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
letters_list= ''.join([ str(elem) for elem in letters])
chiper_shift= int(input('Enter a number to shift your chipher with  '))
print("Print your secret message in letters and spaces only")
secret_message = input('  ')
first_shift= letters_list[26- chiper_shift:26]+letters_list[0:26 - chiper_shift]
second_shift = letters_list[52- chiper_shift:52]+letters_list[26:52 - chiper_shift]
chiper_letters = first_shift+second_shift
# print(chiper_letters)
secret_message = list(secret_message)
chiper_message = []
for i in secret_message:
    new_index = letters_list.find(i)
    if new_index == -1:
        chiper_message = chiper_message+[" "]
    else:
        chiper_message = chiper_message + [chiper_letters[new_index]]

    

chiper_message = ''.join([ str(elem) for elem in chiper_message])
print('this is the new message"', chiper_message , '"')
dechiper_message=[]
for i in chiper_message:
    new_index = chiper_letters.find(i)
    if new_index == -1:
        dechiper_message = dechiper_message+[" "]
    else:
        dechiper_message = dechiper_message + [letters_list[new_index]]

    
print(chiper_message)
dechiper_message = ''.join([ str(elem) for elem in dechiper_message])
print('this is the original message"', dechiper_message , '"')

