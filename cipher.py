import string

letters = string.ascii_lowercase  
num_letters = len(letters)

def encrypt_decrypt(text, mode, shift):
    result = ''
    if mode == 2:
        shift = -shift  

    for letter in text:
        if letter.lower() in letters:
            index = letters.find(letter.lower())
            new_index = (index + shift) % num_letters
            new_letter = letters[new_index]

            result += new_letter
        else:
            result += letter  

    return result

print('CAESAR CIPHER')
print('1. Encrypt')
print('2. Decrypt')
user_input = int(input('Enter Mode : '))

if user_input == 1:
    print('=====> Encryption Mode <=====')
    shift = int(input('Shift (1-26): '))
    text = input('Enter the text for encrypt  : ')
    encrypt = encrypt_decrypt(text, user_input, shift)
    print(f'Result = {encrypt}')

elif user_input == 2:
    print('=====> Decryption Mode <=====')
    print()
    shift = int(input('Shift (1-26): '))
    text = input('Enter the text for decrypt : ')
    decrypt = encrypt_decrypt(text, user_input, shift)
    print(f'Result = {decrypt}')

else:
    print('Sorry, Invalid')