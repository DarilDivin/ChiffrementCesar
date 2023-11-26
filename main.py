def crypt(texte, decalage):
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            resultat += chr((ord(caractere) - ascii_offset + decalage) % 26 + ascii_offset)
        else:
            resultat += caractere
    return resultat


def decrypt(texte, decalage):
    return crypt(texte, -decalage)


# Exemple d'utilisation
print("Que voulez vous faire ??")
print("1. Chiffrer")
print("2. Déchiffrer")
choix = int(input("Veillez entrer 1 ou 2 --> "))

while choix != 1 and choix != 2:
    print("ERREUR...")
    choix = int(input("Veillez entrer 1 ou 2 --> "))

if choix == 1:
    texte_original = input("Entrez le texte à crypter : ")
    decalage_int = int(input("Quel est votre décalage ?? "))
    texte_chiffre = crypt(texte_original, decalage_int)
    print("")
    print("Texte original:", texte_original)
    print("Texte chiffré:", texte_chiffre)
else:
    texte_chiffre = input("Entrez le texte à décrypter : ")
    decalage_int = int(input("Quel est votre décalage ?? "))
    texte_dechiffre = decrypt(texte_chiffre, decalage_int)
    print("")
    print("Texte chiffré:", texte_chiffre)
    print("Texte déchiffré: ", texte_dechiffre)
