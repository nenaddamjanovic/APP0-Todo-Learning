from APP1.bonus.convert import convert
from APP1.bonus.parsers import parse

feet_inches = input("Enter feet in inches: ")

# -------------------------------------------------------------------


parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet and {parsed["inches"]} inches is equal to {result} meters")

if result < 1:
    print("Kid is to small")
else:
    print("Kid can go to slide")
