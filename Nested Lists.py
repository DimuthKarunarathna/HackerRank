"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
The ordered list of scores is , so the second lowest score is .
 There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.


"""
students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2]]
#Answer
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest score
    scores = sorted(set([score for name, score in students]))
    second_lowest = scores[1]

    # Get all names with the second lowest score
    names = [name for name, score in students if score == second_lowest]
    names.sort()

    # Print each name on a new line
    for name in names:
        print(name)