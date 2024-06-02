def calculate_time(h, g=9.80665):
    """
    Funkcija vrši računanje nekog vremena
    :param h:
    :param g:
    :return:
    """
    t = (2 * h / g) ** 0.5
    return t
