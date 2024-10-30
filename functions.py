def get_todo_list(filepath="files/todo.txt"):
    """ Returns the content of the file to use it later """
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def set_todo_list(def_list, filepath="files/todo.txt"):
    """ Modifies the file with a new list """
    with open(filepath, 'w') as file:
        file.writelines(def_list)


if __name__ == "__main__:":
    print("hello from functions")
