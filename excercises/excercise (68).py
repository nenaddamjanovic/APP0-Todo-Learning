filenames = ["a.txt", "b.txt", "c.txt"]

for f in filenames:
    file = open(f, "r")
    content = file.readlines() #izvlači elemnte u formi liste
    print(content)

print("----------")

for f in filenames:
    file = open(f, "r")
    content = file.read() #izvlači elemente u formi stringa ili čega
    print(content)

# reads each text file and
# prints out the content of each file in the command line.