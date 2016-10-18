

def list():
    open_list = open("todos.txt", "r")
    for line in open_list:
        line = line.split(";")
        if len(line) > 1:
            if line[1][0] == "0":
                print("[ ]", line[0])
            elif line[1][0] == "1":
                print("[x]", line[0])

list()            
