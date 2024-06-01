# generates multiple text files by iterating over the filenames list,
# and writes the text Hello  inside each generated text file.

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for f in filenames:
    file = open(f"{f}", "w")
    file.writelines("Hello")
    file.close()

# --------------------------------------------------------------------------

# prompts the user to enter a new member.
# adds that member to members.txt at the end of the existing members.

member_prompt = input("Add a new member: ") #Solomon Right

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append(member_prompt)
file = open("members.txt", "w")
file.writelines(members)
file.close()

# --------------------------------------------------------------------------

# reads each text file and
# prints out the content of each file in the command line.

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
