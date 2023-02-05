if __name__ == '__main__':
    n = int(input("Number: "))
    student_marks = {}
    total = 0
    for _ in range(n):
        name, *line = input("name then score by space: ").split()
        # * variable returns list of inputs (unlimited inputs) confirm by --> print(line)
        #name then score by space: mangu 1 23 76 78
    # ['1', '23', '76', '78']
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Name to find average: ")
    print(student_marks)

    query_list = student_marks[query_name]

    for num in query_list:
        total = total + num 

    avg = total / len(query_list)
      
        
    print(f"The Average marks for {query_name} is {avg:.2f}")
    # avg: .2f means round it off to 2 decimal places.

    # --------------------------------------------------------------------------------------------------------------------
    
 N = int(input())
STUDENT_MARKS = {}

for line in range(N):
    info = input().split(" ")
    grades = list(map(float, info[1:]))
    STUDENT_MARKS[info[0]] = sum(grades) / float(len(grades))

print("%.2f" % round(STUDENT_MARKS[input()], 2))

