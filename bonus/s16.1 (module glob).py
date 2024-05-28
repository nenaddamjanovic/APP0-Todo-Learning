import glob

myfiles = glob.glob("files/*.txt")
print(f"This is all of my files: {myfiles}\n")

for index, filepath in enumerate(myfiles):
    with open(filepath, "r") as file:
        print(f"{index} --- {filepath}:\n{file.read()}")
