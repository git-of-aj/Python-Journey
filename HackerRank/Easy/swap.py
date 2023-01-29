def swap_case(s):
    SwAp = ''
    # one by one take characters present in s
    for char in s:
        # if the picked character is not alreday in upper case..
        if char.upper() != char:
            SwAp += char.upper() 
            # this makes it upper case & adds it to
            # the empty string... 
        else:
            char.lower() != char
            SwAp += char.lower()
    return SwAp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
    # -----------------------------------
    
    ''' Using build in  String Mehod --> swap case '''
    
sentence = input("enter: ")
print(sentence.swapcase())
