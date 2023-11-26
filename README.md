# Algorithme du chiffrement de César en Python

Le code de César est un algorithme de chiffrement par substitution dans lequel chaque lettre dans le texte est déplacée d'un certain nombre de positions dans l'alphabet. Voici une explication du fonctionnement de l'algorithme de César en Python.

## Fonction de Chiffrement César

La fonction de chiffrement César (`crypt`) prend une chaîne de caractères et un décalage comme arguments. Elle chiffre chaque lettre alphabétique de la chaîne en utilisant le décalage spécifié.

```python
def crypt(texte, decalage):
    resultat = ""
    for caractere in texte:
        if caractere.isalpha():
            ascii_offset = ord('A') if caractere.isupper() else ord('a')
            resultat += chr((ord(caractere) - ascii_offset + decalage) % 26 + ascii_offset)
        else:
            resultat += caractere
    return resultat
```

- La boucle `for` itère à travers chaque caractère de la chaîne `texte`.
- La condition `if caractere.isalpha():` vérifie si le caractère est une lettre alphabétique.
- La variable `ascii_offset` est définie en fonction de la casse du caractère, pour normaliser le code ASCII.
- La formule ``(ord(caractere) - ascii_offset + decalage) % 26 + ascii_offset`` calcule la nouvelle position de la lettre après le décalage, en tenant compte du rebouclage à travers l'alphabet.
- Les caractères non alphabétiques restent inchangés.

## Exemple d'Utilisation

Un exemple d'utilisation du chiffrement César est donné ci-dessous :

```python
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
```

Dans ce exemple, il est demandé à l'utilisateur ce qu'il veut faire.
Il a deux choix :
- Chiffrer 
  > On lui demande de fournir le texte qu'il veut chiffrer puis le décalage
  >
  > Le texte est alors chiffrer et on le lui affiche.
- Déchiffrer 
  > On lui demande de fournir le texte qu'il veut déchiffrer puis le décalage
  >
  > Le texte est alors déchiffrer et on le lui affiche.
