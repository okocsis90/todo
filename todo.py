import os.path

#mark function :) (mano)
def mark(id):

    #list for the todos
    todos = []

    #opening the todo file and loading the elements into the list
    with open('todos.txt', "r") as todosf:
        for todo in todosf:
            todos.append(todo.strip().split(";"))
        todosf.close()
    
    #check if id is valid. if yes do the change
    if (id <= len(todos) and id > 0):
        todos[id-1][1] = 1
        print(todos[id-1][0]+" is completed")
    
    #convert the list to the string we have to save into the txt
    string = ""
    for i in range(0,len(todos)):
        string += todos[i][0]+";"+str(todos[i][1])+"\n"
    
    #write out the file
    fopen = open("todos.txt", "w")
    fopen.write(string)
    fopen.close()

#archive function :) (mano)
def archive():

    #list for todos
    todos = []

    #opening the todo file and loading the elements into the list
    with open('todos.txt', "r") as todosf:
        for todo in todosf:
            todos.append(todo.strip().split(";"))
        todosf.close()
    
    #string for the write
    string = ""

    #now converting the new string without the finished todos
    for i in range(0,len(todos)):
        if str(todos[i][1]) != "1":
            string += todos[i][0]+";"+str(todos[i][1])+"\n"
    
    #write out the file
    fopen = open("todos.txt", "w")
    fopen.write(string)
    fopen.close()
    
    #print message
    print("All completed tasks got deleted.")

#listing out the elements (peti)
def list():
    print("You saved the following to-do items:")
    open_list = open("todos.txt", "r")
    hereIam = 1
    for line in open_list:
        line = line.split(";")
        if len(line) > 1:
            if line[1][0] == "0":
                print(str(hereIam)+".", "[ ]", line[0])
            elif line[1][0] == "1":
                print(str(hereIam)+".", "[x]", line[0])
        hereIam += 1
    open_list.close()

#adding a new item
def add():
    todo = open("todos.txt", "a")

    add_element_to_list = input("Add an item: ")
    to_add = add_element_to_list + ";0\n"
    s = str(to_add)
    todo.write(s)
    todo.close()
    print("Item added.")

#if todos.txt doesnt exists we crate it
if os.path.exists("todos.txt") == False:
    fopen = open("todos.txt", "w")
    fopen.write("")
    fopen.close()

while 1==1:
    #kérjük be milyen feladatot várunk tőle
    command = input("Please specify a command [list, add, mark, archive, close]: ")

    #if else ág a commandok lekezelésére
    if command == "list":
        list()
    elif command == "add":
        add()
    elif command == "mark":
        list()
        id = input("Which one you want to mark as completed: ")
        mark(int(id))
    elif command == "archive":
        archive()
    elif command == "close":
        break