N = int(input("Total Inputs: "))
operations_list = []

def list_operations():

    if method == 'insert':
        return operations_list.insert(index,number)
    
    if method == 'append':
        return operations_list.append(number)

    if method == 'remove':
        return operations_list.remove(number)

    if method == 'pop':
        return operations_list.pop()

    if method == 'sort':
        return operations_list.sort()

    if method == 'reverse':
        return operations_list.reverse()
    
    if method == 'print':
        print(operations_list)

for _ in range(N):
    usr_input = input("Method then index then number etc: ").split()
    method = usr_input[0]

    if len(usr_input) == 3:
        index = int(usr_input[1])
        number = int(usr_input[2])
    
    elif len(usr_input) == 2:
        number = int(usr_input[1])       

    list_operations()
#print(usr_input,operations_list,sep='\n')

