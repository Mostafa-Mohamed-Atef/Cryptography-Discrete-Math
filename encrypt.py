alphabet_dict = {chr(97 + i): i for i in range(26)}
sentence = input('Enter your message : \n').strip(' ').split(' ')
encrypted = []
decrypted = []
E = tt = original = ""

def Encryption():
    global E, tt, encrypted
    for word in sentence:
        for letter in word:
            encrypted.append(alphabet_dict[letter])
    for x in range(len(encrypted)):
        E += str((encrypted[x] + 11) % 26) + " "
    print(E)
    E2 = list(map(int,E.strip(' ').split(' ')))
    for y in range(len(E2)):
        for key, value in alphabet_dict.items():
            if value == E2[y]:
                tt += key 
    print(tt)
    E = E2 = ""

def Decryption():   
    global E, tt, decrypted, original
    for word in tt:
        for letter in word:
            decrypted.append(alphabet_dict[letter])
    for x in range(len(decrypted)):
        E += str((decrypted[x] - 11) % 26) + " "
    # print(E)
    E2 = list(map(int,E.strip(' ').split(' ')))
    for y in range(len(E2)):
        for key, value in alphabet_dict.items():
            if value == E2[y]:
                original += key 
    print(original)



Encryption()
Decryption()

