member_prompt = input("Add a new member: ") #Solomon Right

file = open("members.txt", "r")
members = file.readlines()
file.close()

members.append(member_prompt)
file = open("members.txt", "w")
file.writelines(members)
file.close()

# prompts the user to enter a new member.
# adds that member to members.txt at the end of the existing members.
