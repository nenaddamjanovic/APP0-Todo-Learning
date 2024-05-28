filenames = ["1.my_folder.dir", "2.my_photos.jpg", "3.my_songs.mp3"]
print(filenames)

#samo prividno menja, ali ne čva u listi izmenu
for filename in filenames:
    filename = filename.replace(".", "-", 1)
    print(filename)

#ovo menja  i čuva izmenu lsite
for i in range(len(filenames)):
    filenames[i] = filenames[i].replace(".", "-", 1)

print(filenames)