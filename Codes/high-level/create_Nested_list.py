def main():
    students = []
    scores = []
    for _ in range(int(input("Total: "))):
        name = input("Name: ")
        score = float(input("Score: "))
        student = [name, score]
        students.append(student)
        scores.append(score)
    print("This is student----> ",student,sep="\n")
    print("This is students----> ",students,sep='\n')
    print("This is scores----> ",scores,sep="\n")

if __name__ == '__main__':
    main()
    
    """
  OUTPUT:
  Name: papa
Score: 734
This is student---->
['papa', 734.0]
This is students---->
[['appa', 73.0], ['mamma', 843.0], ['papa', 734.0]]
This is scores---->
[73.0, 843.0, 734.0]
    """
