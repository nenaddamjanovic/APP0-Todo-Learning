try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    if width == length:
        exit("That looks like a square, not rectangle")

    area = width * length
    print(f"The area of rectangle is: {area}")
except ValueError:
    print("Please enter only numbers")