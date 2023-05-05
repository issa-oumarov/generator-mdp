import hashlib


input_hashed = input('Saisir mdp crypté:' )

with open('passwords.txt', 'r', encoding='utf-8') as passwords_file:

    try:
        for password in passwords_file:
            encoding_password = password.strip().encode('utf-8')
            hashed_password = hashlib.md5(encoding_password)
            digesting = hashed_password.hexdigest()
        
            print("Mot de passe dans le fichier: ", password)
            print("Hachage du mot de passe: ", digesting)

            if digesting == input_hashed:
                print('mdp decrypté: ' , password)
                passwords_file.close()
                break 

    except:
        print('mdp non trouver')
        passwords_file.close()
