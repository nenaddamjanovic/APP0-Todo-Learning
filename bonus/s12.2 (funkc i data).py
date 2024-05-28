def get_average():
    with open("../files/data.txt", "r") as file:
        data = file.readlines()  # readlines isčitava kao listu elemenata
    values = data[1:]  # Nećemo prvi element, to je naslov
    values = [float(i) for i in values]  # Pretvaramo elemente u brojeve
    average_temp = sum(values) / len(values)
    return f"Average temperature in data.txt file is: {average_temp}"  # i tu može fstring


#average = get_average()
#print(average)

print(get_average())