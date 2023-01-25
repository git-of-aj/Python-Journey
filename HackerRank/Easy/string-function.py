def split_and_join(line):
    # converts into a list of words seperated by delimiter --> " "
    seperate = line.split(" ")
    #  joins the list back again into a string with - 
    return "-".join(seperate)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
