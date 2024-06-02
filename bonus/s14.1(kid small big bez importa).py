feet_inches = input("Enter feet in inches: ")


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


def convert(feet, inches):
    """
    Funkcija vrši pretvaranje sopa i inča u metre
    :param feet:
    :param inches:
    :return:
    """
    meters = feet * 0.3048 + inches * 0.0254
    return meters


# -------------------------------------------------------------------


parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet and {parsed["inches"]} inches is equal to {result} meters")

if result < 1:
    print("Kid is to small")
else:
    print("Kid can go to slide")
