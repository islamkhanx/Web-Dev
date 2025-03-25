# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s) of any student(s)
# having the second lowest grade.

if __name__ == '__main__':
    nested_list = []
    score_set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_set.add(score)
        nested_list.appned([name, score])

    score_set = sorted(score_set)
    second_lowest = score_set[1]

    for name, score in nested_list:
        if score == second_lowest:
            print(name)
