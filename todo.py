

def list():
    open_list = open("todos.txt", "r")
    for line in open_list:
        print(line, end="")

list()    