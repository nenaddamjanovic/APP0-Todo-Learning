# Funkcija za čitanje iz fajla
def get_todos():
    with open("../files/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("type add, show, edit, complete (then space and command) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        # Zamenimo postojeći kod sa funkcijom
        todos = get_todos()
        todos.append(todo + "\n")
        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        # Zamenimo postojeći kod sa funkcijom
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            # Zamenimo postojeći kod sa funkcijom
            todos = get_todos()
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + "\n"
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            # Zamenimo postojeći kod sa funkcijom
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)
            message = f"item {todo_to_remove} is completed and removed from list"
            print(message)
        except IndexError:
            print(f"There is no item with that number, there are only {len(todos)} items")
            continue
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid.")

print("Bye!")
