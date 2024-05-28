def without_return():
    message = "Hello"
    new_message = message.capitalize()
    print("Hey hey")  # print nije return!


def with_return():
    message = "Hello"
    new_message = message.capitalize()
    return new_message


def maths_calc(a,b):
    # račuanje razno
    result1 = float(a * b)
    result2 = float(a ** b)
    result3 = float(a / b)
    return f"multiplication:{result1} - exponent:{result2} - divide:{result3}"


def greet(message):
    new_message = message.capitalize()
    return new_message

# ----------------------------------------------------------------------------

greeting = without_return()
# Vraća samo print iz funkcije
print(greeting)
# Ovakva funkicja faktički ne vraća nikakvu vrednost ni akciju - None

print()  # --------------------------------------------------------------------

greeting2 = with_return()
print(greeting2)
# Ovo je normalna funkcija koja prvo vraća, pa printa šta treba

print()  # --------------------------------------------------------------------

maths = maths_calc(104,4)
print(maths)

print()  # --------------------------------------------------------------------

user_entry = input("what greeting do you want: ")
greeting = greet(user_entry)
print(greeting)