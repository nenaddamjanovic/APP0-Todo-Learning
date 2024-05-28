for index,letter in enumerate("Velikareč"):
    print(index, letter)
print()

for i,j in enumerate("Velikareč"):
    print(i+1,j)
print()

car_brands = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
              "BMW", "Mercedes-Benz", "Audi", "Nissan", "Tesla"]
car_brands.sort()
for index, car in enumerate(car_brands):
    print(f"{index + 1}-{car}")
print()

#enumerated metod daje listu parova torki.
enumerated_list = enumerate(["a","b","c","d","e","f","g"])
print(list(enumerated_list))
print()

for i, item in [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g')]:
    print(i, item)


