alphabet_dict = {chr(97 + i): i for i in range(26)}
sentence = input('Enter your message: \n')

encrypted_text = encrypted_numbers =  original = ""
encrypted_value = 0

def Encryption():
    global encrypted_text, encrypted_numbers, encrypted_value
    for letter in sentence:
        if letter == ' ':
            encrypted_text += ' '
            encrypted_numbers += ' '
        else:
            encrypted_value = (alphabet_dict[letter] + 11) % 26
            encrypted_numbers += str(encrypted_value) + " "
            encrypted_letter = chr(97 + encrypted_value)
            encrypted_text += encrypted_letter
    print(f'Encrypted numbers ===> {encrypted_numbers}')
    print(f"Encrypted Message ===> {encrypted_text}")
    encrypted_numbers = ""

def Decryption():
    global encrypted_text, encrypted_numbers, original, encrypted_value
    for letter in encrypted_text:
        if letter == ' ':
            original += ' '
            encrypted_numbers += ' '
        else:
            encrypted_value = (alphabet_dict[letter] - 11) % 26
            encrypted_numbers += str(encrypted_value) + " "
            encrypted_letter = chr(97 + encrypted_value)
            original += encrypted_letter
    print(f"Decrypted Numbers ===> {encrypted_numbers}")
    print(f"Decrypted Message(orignal) ===> {original}")

Encryption()
Decryption()