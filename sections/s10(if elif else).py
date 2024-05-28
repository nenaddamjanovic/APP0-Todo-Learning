
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

#zamenjeni match case, sa if petljama, i in metodom.
    #operator or
    if "add" in user_action or "new" in user_action or "more" in user_action:
        #ovo izvlači sve što user upisuje ali bez prvih 4 karaktera, tj add .
        todo = user_action[4:]
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_action:
        #hoćemo da program izvlači sve iz jedne linije unosa
        number = int(user_action[5:])
        print(number)
        number = number - 1
        with open("../files/todos.txt", "r") as file:
            todos = file.readlines()
        new_todo = input("enter new todo: ")
        todos[number] = new_todo + "\n"
        with open("../files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        # hoćemo da program izvlači sve iz jedne linije unosa
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

    elif "exit" in user_action:
        break

    else:
        print("command is not valid.")

print("Bye!")