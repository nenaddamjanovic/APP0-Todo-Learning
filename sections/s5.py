todos = []

while True:
    user_action = input("type add, show(display), edit, complete or exit: ")
    # brišemo spejsove oko inputa
    user_action = user_action.strip()
    # sada se program pita da uporedi šta je upisao korisnik u user_action
    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            # printamo stavke u listi pojedinačno, a ne da se vide [] kao običa print liste
            for item in todos:
                item = item.title()
                print(item)
        case "edit":
            number = int(input("number of todo item in list: "))
            number = number - 1 # zato što index liste počinje od 0
            # sada upisujemo novi input u mesto starog elementa
            new_todo = input("enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break
        case _: # piše se _ jel je to nebitna promenljiva koja se kreira u tom trenutku i ne služi ničemu drugom
            print("please enter only listed commands")

print("Bye!")