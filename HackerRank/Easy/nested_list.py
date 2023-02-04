def main():
  final_list = []
    score_list = []
    name_list = []
    for _ in range(int(input("TOtal Students: "))):
        name = input("Name: ")
        score = float(input("Score: "))

        score_list.append(score)

        initial_list = [name,score]
        final_list.append(initial_list)
    #print(final_list) to confirm it's working

# beacuse sorted() returns a list of ascending order items, get second lowest .... get index 1 = [1]
# like = [78.0, 78.2, 78.9] --> will be result of sorted
    second_lowest = sorted(score_list)[1]

    for name,grade in final_list:
        if grade == second_lowest:
            name_list.append(name)

    for name in sorted(name_list):
        print(name)
        
main()
