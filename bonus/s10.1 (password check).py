# Program za proveru jačine šifre
password = input("Enter your password: ")
result = {}

# Proveravamo da li šifra ima određenu dužinu
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

# Proveravamo da li ima brojeve u šifri
digit = False
for p in password:
    if p.isdigit():
        digit = True
result["digit"] = digit

# Proveravamo ima li uper case u šifri
uppercase = False
for p in password:
    if p.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)
# funkcija all() daje True ako su svi uslovi True
# if all(result) == True:  Ovo je uprošćeno dole
if all(result.values()):
    print("Password is strong")
else:
    print("Password is weak")
