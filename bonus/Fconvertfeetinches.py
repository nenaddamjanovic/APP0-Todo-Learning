def convert(feet, inches):
    """
    Funkcija vrši pretvaranje sopa i inča u metre
    :param feet:
    :param inches:
    :return:
    """
    meters = feet * 0.3048 + inches * 0.0254
    return meters
