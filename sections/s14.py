def get_todos(filepath="files/todos.txt"):
    """
    Read a text file and return the list by to-do items
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):  # Defaultni parametri, prvo idu promenljivi, posle defaultni
    """
    Write the to-do items list in the text file
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

#  -----------------------------------------------------------------------------


while True:
    user_action = input("type add, show, edit, complete (then space and command) or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()  # Ne treba parametar, ima default
        todos.append(todo + "\n")
        write_todos(todos)  # Ne treba drugi parametar, ima default

    elif user_action.startswith("show"):
        todos = get_todos()  # Ne treba parametar, ima default
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = get_todos()  # Ne treba parametar, ima default
            new_todo = input("enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)  # Ne treba drugi parametar, ima default
        except ValueError:
            print("Your command is not valid, format is ACTION NUMBER")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()  # Ne treba parametar, ima default
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)  # Ne treba drugi parametar, ima default
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
