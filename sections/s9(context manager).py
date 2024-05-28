
while True:
    user_action = input("type add, show(display), edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"

            # file = open("files/todos.txt", "r")
            # todos = file.readlines()
            # file.close()
        # CONTEXT MANAGER - Bolja opcija od opcije gore
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show" | "display":
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
        # OPCIJA C - najlakša opcija
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("number of todo item in list: "))
            number = number - 1
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + "\n"
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            number = int(input("number of todo item to complete: "))
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            print(f"item {todo_to_remove} is completed and removed from list")
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break

        case _:
            print("please enter only listed commands")

print("Bye!")