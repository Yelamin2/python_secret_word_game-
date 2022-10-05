from ast import Break, Return


letters= ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
letters_list= ''.join([ str(elem) for elem in letters])
cipher_shift= int(input('Enter a number to shift your cipher with  '))

print("Print your secret message in letters and spaces only")

secret_message = input('  ')
first_shift= letters_list[26- cipher_shift:26]+letters_list[0:26 - cipher_shift]
second_shift = letters_list[52- cipher_shift:52]+letters_list[26:52 - cipher_shift]
cipher_letters = first_shift+second_shift
# print(cipher_letters)
secret_message = list(secret_message)
cipher_message = []
for i in secret_message:
    new_index = letters_list.find(i)
    if new_index == -1:
        cipher_message = cipher_message+[i]
    else:
        cipher_message = cipher_message + [cipher_letters[new_index]]

cipher_message = ''.join([ str(elem) for elem in cipher_message])
print('this is the new message"', cipher_message , '"')
decipher_message=[]
for i in cipher_message:
    new_index = cipher_letters.find(i)
    if new_index == -1:
        decipher_message = decipher_message+[i]
    else:
        decipher_message = decipher_message + [letters_list[new_index]]

    
print(cipher_message)
decipher_message = ''.join([ str(elem) for elem in decipher_message])
print('this is the original message"', decipher_message , '"')

