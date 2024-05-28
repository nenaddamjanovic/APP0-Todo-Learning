todos = []

while True:
    user_action = input("type add, show, exit: ")
    # sada se program pita da uporedi šta je upisao korisnik u user_action
    match user_action:
        case "add":
            todo = input("enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break

print("Bye!")