import hashlib


PASSWORDS_FILE = "passwords.txt"

def add_password():
    while True:
        password = input("Veuillez saisir un mot de passe: ")
        if (len(password) < 6 or not any(char.isupper() for char in password)
                or not any(char.islower() for char in password) or not any(char.isdigit() for char in password)
                or not any(char in "!@#$%^&*." for char in password)):
            print("Le mot de passe ne répond pas aux exigences de sécurité.")
        else:
            hash_object = hashlib.md5(password.encode())
            hashed_password = hash_object.hexdigest()
            with open(PASSWORDS_FILE, "r") as f:
                passwords = f.readlines()
                if hashed_password + "\n" in passwords:
                    print("Ce mot de passe a déjà été enregistré.")
                    break
            with open(PASSWORDS_FILE, "a") as f:
                f.write(hashed_password + "\n")
            print("Le mot de passe a été ajouté avec succès.")
            break


def view_passwords():
    try:
        with open(PASSWORDS_FILE, "r") as f:
            passwords = f.readlines()
            if len(passwords) == 0:
                print("Il n'y a aucun mot de passe enregistré.")
            else:
                print("Liste de tous les mots de passe enregistrés : ")
                for password in passwords:
                    print(password.strip())
    except FileNotFoundError:
        print("Il n'y a aucun mot de passe enregistré.")

while True:
    choice = input("Voulez-vous ajouter un nouveau mot de passe (1) ou afficher la liste des mots de passe enregistrés (2) ? ")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    else:
        print("Option invalide.")

