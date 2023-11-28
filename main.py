def mod_inverse(a, m):
    # Calcul de l'inverse modulaire de a modulo m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def chiffrement_affine(plaintext, a, b):
    # Taille de l'alphabet (26 pour l'alphabet français)
    m = 26
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            # Conversion de la lettre en valeur numérique
            x = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')

            # Application de la fonction de chiffrement affine
            y = (a * x + b) % m

            # Conversion de la valeur numérique en lettre
            lettre_chiffree = chr(y + ord('A')) if char.isupper() else chr(y + ord('a'))
            ciphertext += lettre_chiffree
        else:
            # Si la caractère n'est pas une lettre, le laisser inchangé
            ciphertext += char

    return ciphertext


def dechiffrement_affine(ciphertext, a, b):
    # Calcul de l'inverse modulaire de a modulo 26
    m = 26
    a_inverse = mod_inverse(a, m)

    if a_inverse is None:
        raise ValueError("Inverse modulaire de 'a' n'existe pas.")

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            # Conversion de la lettre en valeur numérique
            y = ord(char) - ord('A') if char.isupper() else ord(char) - ord('a')

            # Application de la fonction de déchiffrement affine
            x = (a_inverse * (y - b)) % m

            # Conversion de la valeur numérique en lettre
            lettre_dechiffree = chr(x + ord('A')) if char.isupper() else chr(x + ord('a'))
            plaintext += lettre_dechiffree
        else:
            # Si le caractère n'est pas une lettre, le laisser inchangé
            plaintext += char

    return plaintext


# Exemple d'utilisation
"""texte_clair = "NSA"
u = 3
v = 11

texte_chiffre = chiffrement_affine(texte_clair, u, v)
print("Texte chiffré:", texte_chiffre)

texte_dechiffre = dechiffrement_affine(texte_chiffre, u, v)
print("Texte déchiffré:", texte_dechiffre)"""

print("Que voulez vous faire ??")
print("1. Chiffrer")
print("2. Déchiffrer")
choix = int(input("Veillez entrer 1 ou 2 --> "))

while choix != 1 and choix != 2:
    print("ERREUR...")
    choix = int(input("Veillez entrer 1 ou 2 --> "))

if choix == 1:
    texte_original = input("Entrez le texte à crypter : ")
    u = int(input("Entrer a: "))
    v = int(input("Entrer b: "))
    texte_chiffre = chiffrement_affine(texte_original, u, v)
    print("")
    print("Texte original:", texte_original)
    print("Texte chiffré:", texte_chiffre)
else:
    texte_chiffre = input("Entrez le texte à décrypter : ")
    u = int(input("Entrer a: "))
    v = int(input("Entrer b: "))
    texte_dechiffre = dechiffrement_affine(texte_chiffre, u, v)
    print("")
    print("Texte chiffré:", texte_chiffre)
    print("Texte déchiffré: ", texte_dechiffre)
