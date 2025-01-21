import matplotlib.pyplot as plt

class Student:        
    def __init__(kid, name):
        kid.name = name
        kid.grades = {}
        kid.average_grade = 0.0
    
    def add_grade(kid, subject_name, grade):
        if subject_name in kid.grades.keys():
            kid.grades[subject_name].append(grade)
        else:
            kid.grades[subject_name] = []
            kid.grades[subject_name].append(grade)
    
    def get_average(kid, subject_name):
        return sum(kid.grades[subject_name]) / len(kid.grades[subject_name])
    
    def get_overall_average(kid):
        total = 0.0
        for i in kid.grades.values():
            total += sum(i) / len(i)
        return total / len(kid.grades)
    
    def highest_grade(kid):
        all_grades = []
        for i in kid.grades.values():
            for j in i:
                all_grades.append(j)
        all_grades.sort()
        return all_grades[-1]

    def visualize_grades(kid):
        datapoints = []
        for i in kid.grades.values():
            for j in i:
                datapoints.append(j - 0.1)
        plt.hist(datapoints, bins = [0.9, 1.1, 1.9, 2.1, 2.4, 2.6, 2.9, 3.1, 3.4, 3.6, 3.9, 4.1])
        plt.xlabel("Grades")
        plt.ylabel("Frequency")
        plt.title(f"Grade Distribution for {kid.name}")
        plt.show()