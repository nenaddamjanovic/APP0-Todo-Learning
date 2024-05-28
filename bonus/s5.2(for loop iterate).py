names_lists = [
    ["Alice", "Bob", "Charlie", "David"],
    ["Eva", "Frank", "Grace", "Hannah"],
    ["Isaac", "Jack", "Katie", "Liam"],
    ["Mia", "Noah", "Olivia", "Peter"],
    ["Quinn", "Rachel", "Sophie", "Tyler"],
    ["Victoria", "William", "Xavier", "Yvonne"]
]
for a, b, c, d in names_lists:
    print(a, b, c, d)
print("_____________")
for a, b, c, d in names_lists:
    print(c, d)
print("_____________")
for a, b, c, d in names_lists:
    print(d, a, c)
print("_____________")
for a, b, c, d in names_lists:
    print(c)
print("_____________")