def rectangle (longeur,largeur) :
    """
    fonction qui calcule l'aire d'un réctangle
    longeur * largeur
    retourne l'aire ...
    """
    aire = longeur * largeur
    return aire

def prixTTC (prix) :
    """
    fonction qu calcule la taxe sur un prix TTC
    on calcule la taxe en multipliant prix par 1.203
    prix : float > 0
    retourne tax : float
    """
    tax = prix * 1.206
    return tax

help(prixTTC)
help(rectangle)