date = input("Please enter today´s date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Write your thoughts:\n")

with open(f"files/{date}.txt", "w") as file:
    file.write(f"Mine current mood: {mood}.\n")
    file.write(f"My thoughts for the day: ´{thoughts}´")


# If you want to get all the text as one single string, use read().
# If you want to get separate strings for each line, use readlines().