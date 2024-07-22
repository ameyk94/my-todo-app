FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Read a text and returns the list of
    todo items in text file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath='todos.txt'):
    """ Write the to-do items list in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
