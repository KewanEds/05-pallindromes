"""Permet de tester si une chaîne de caractère est un palindrome
"""
def ispalindrome(p):
    """Mets la chaîne de caractère en minuscule et supprime les caractères indésirables.
    Test ensuite l'égalité
    """
    p = p.lower()
    p = p.translate(str.maketrans("éèêëàâäîïôöùûüç","eeeeaaaiioouuuc"," &_-([{)]}=+°?.,;:!¨*'"))
    s = p[::-1]
    return s == p

#### Fonction principale


def main():
    """Appelle la fonction secondaire ispalindrome et la test
    """
    print(ispalindrome("bonjour"))
    print(ispalindrome("racecar"))

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
