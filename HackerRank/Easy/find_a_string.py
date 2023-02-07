def count_substring(string, sub_string):
    i = string.find(sub_string)
    count = 0 
    while i != -1:
        count += 1
        # i = index of the substring
        # i + 1 = skip this move to next one
        i = string.find(sub_string,i+1)
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
