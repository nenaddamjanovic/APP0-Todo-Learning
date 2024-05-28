
while True:
    user_action = input("type add, show(display), edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            # funkcija .readlines radi otvaranje fajla todos.txt
            file = open("../files/todos.txt", "r")
            # dodeljuje sve iz fajla u listu todos
            todos = file.readlines()
            file.close() #mora da se zatvori fajl
            # dodajemo na postojeću listu, ono što je korisnik dodao
            todos.append(todo)
            # funkcija .writelines radi upisivanje u fajl todos.txt
            file = open("../files/todos.txt", "w")
            file.writelines(todos)
            file.close()  # mora da se zatvori fajl
        case "show" | "display":
            # moramo i ovde da otvorimo todos iz fajla
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            # printamo stavke u listi pojedinačno, a ne da se vide [] kao običa print liste
            for index, item in enumerate(todos): #metod enumerate prebraja listu
                item = item.title()
                row = f"{index + 1}-{item}"
                print(row)
            # print("hello", index, item)
        case "edit":
            number = int(input("number of todo item in list: "))
            number = number - 1 # zato što index liste počinje od 0
            # sada upisujemo novi input u mesto starog elementa
            new_todo = input("enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("number of todo item to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _: # piše se _ jel je to nebitna promenljiva koja se kreira u tom trenutku i ne služi ničemu drugom
            print("please enter only listed commands")

print("Bye!")