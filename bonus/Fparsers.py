def parse(feet_inches):
    """
    Funkcija vraća vrednosti u obliku rečnika
    :param feet_inches:
    :return:
    """
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}
