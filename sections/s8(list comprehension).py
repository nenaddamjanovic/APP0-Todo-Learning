
while True:
    user_action = input("type add, show(display), edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("../files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open("../files/todos.txt", "r")
            todos = file.readlines()
            file.close()
        #print(todos)#vidimo da se printa znak \n na kraju

        # OPCIJA A - kreiramo novu listu i nove iteme, ali oni nemaju \n na kraju
            # new_todos = []
            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

        # OPCIJA B - list compenhension za for petlju gore
            # new_todos = [item.strip("\n") for item in todos]

        # NASTAVAK A,B - sada u pregledu show petlja ide kroz novu listu
            # for index, item in enumerate(new_todos):
            #     row = f"{index + 1}-{item}"
            #     print(row)

        # OPCIJA C - najlakša opcija
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("number of todo item in list: "))
            number = number - 1
            new_todo = input("enter new todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("number of todo item to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("please enter only listed commands")

print("Bye!")