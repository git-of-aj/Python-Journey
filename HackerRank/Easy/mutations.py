# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def mutate_string(string,position,character):
    new_list = list(string)
    new_list[position] = character
    return ''.join(new_list)
    
if __name__ == '__main__':
    string = input("Please enter series of chars: ")
    # by default split takes whitespace as a seperator
    pos,char = input("Pls enter poistion then space character to replace: ").split()
    print(mutate_string(string,int(pos),char))
    
