FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    reads in a file and returns the list of todos.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH):
    """Writes the todos list to a text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

