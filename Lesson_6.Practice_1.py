my_dict = dict(Ivanov = [10, 12, 9], Ivanov2 = [12, 8, 7], Ivanov3 = [7, 8, 9])

best_student_name = ''
worst_student_name = ''
best_student_av = 0
worst_student_av = 100

for key, value in my_dict.items():
    average_points = sum(value) / len(value)
    if average_points > best_student_av:
        best_student_name = key
        best_student_av = average_points
    if average_points < worst_student_av:
        worst_student_name = key
        worst_student_av = average_points
print(best_student_name, best_student_av, worst_student_name, worst_student_av)