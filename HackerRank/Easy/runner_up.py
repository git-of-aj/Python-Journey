# convert the input into set to remove duplicate values
# sort the list in reverse order
# find the list item with index 1, 0 being the first appearance

def main():
    arr = map(int, input("give numbers: ").split())
    print(sorted(set(arr), reverse=True)[1])

main()
