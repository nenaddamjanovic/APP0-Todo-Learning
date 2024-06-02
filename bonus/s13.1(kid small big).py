feet_inches = input("Enter feet in inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")  # Razdvajamo input korisnika na space
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert(feet_inches)

if result < 1:
    print("Kid is to small")
else:
    print("Kid can go to slide")
