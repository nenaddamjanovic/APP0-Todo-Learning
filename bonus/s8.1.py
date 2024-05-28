filenames = ["1.doc", "1.report", "1.presentation"]
print(filenames)
# menjamo sadržaj stringova u 1-doc.txt funkcijom replace("find what", "replace with")
filenames = [filename.replace(".", "-") + ".txt" + "blablabla" for filename in filenames]

print(filenames)

# ----------------------------------------------------

# # primer sa list comprehension
# numbers = ["10", "19.1", "20"]
# float_numbers = [float(num) for num in numbers]
# print(float_numbers)
#
# # primer sa for petljom
# numbers = ['10', '19.1', '20']
# float_numbers = []
# for num in numbers:
#     num = float(num)
#     float_numbers.append(num)
# print(float_numbers)

# ---------------------------------------------------

# # suma elemenata liste
# user_entries = ['10', '19.1', '20']
# sum_numbers = sum([float(i) for i in user_entries])
# print(sum_numbers)
