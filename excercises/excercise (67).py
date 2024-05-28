filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for f in filenames:
    file = open(f"{f}", "w")
    file.writelines("Hello")
    file.close()

# generates multiple text files by iterating over the filenames list,
# and writes the text Hello  inside each generated text file.