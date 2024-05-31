import random

user_number_1 = int(input("Please enter first number, from 0 - 100: "))
user_number_2 = int(input("Please enter second number, from 0 - 100: "))

if user_number_2 < user_number_1 < 100:
    gen_number = random.randrange(user_number_2, user_number_1)
    print(f"random generated number is: {gen_number}")
else:
    print("Please enter first number higher then second, and less then 100")
