#file = open (r"C:\Users\Nenad\OneDrive\Radna površina\python_work\poglavlje1", "w")
#r se postavlja ispred stringa kako bi python znao da negleda spec. oznake pr \n


#program koji upisuje vrednosti iz liste contents u fajlove kao u listi filenames
#koristi se zip() funkcija koja pravi parove elemenata iz dve liste
contents = ["slicing carrots in half",
            "now we slice onions and cry",
            "and now we cook them in a pan"]
filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)