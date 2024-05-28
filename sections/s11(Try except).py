while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # poboljšani input i prihvatanje od korisnika .startswith()
    if user_action.startswith("add"):
        todo = user_action[4:]
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo + "\n")
        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

    # poboljšani input i prihvatanje od korisnika .startswith()
    elif user_action.startswith("show"):
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    # poboljšani input i prihvatanje od korisnika .startswith()
    elif user_action.startswith("edit"):
        try:  # Pokušava ovu sekciju
            number = int(user_action[5:])
            print(number)
            number = number - 1
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + "\n"
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:  # Ako je greška ovakva izvrašava dole
            print("Your command is not valid, format is ACTION NUMBER")
            continue  # Vraća na početak while petlje

    # poboljšani input i prihvatanje od korisnika .startswith()
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("../files/todos.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("../files/todos.txt", "w") as file:
                file.writelines(todos)
            message = f"item {todo_to_remove} is completed and removed from list"
            print(message)
        except IndexError:
            print(f"There is no item with that number, there are only {len(todos)} items")
            continue  # Vraća na početak while petlje
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue  # Vraća na početak while petlje

    # poboljšani input i prihvatanje od korisnika .startswith()
    elif user_action.startswith("exit"):
        break

    else:
        print("command is not valid.")

print("Bye!")