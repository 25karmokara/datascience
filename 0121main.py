import student
import matplotlib.pyplot as plt

def is_anagram(str1, str2):
    sorted1 = ''.join(sorted(str1))
    sorted2 = ''.join(sorted(str2))
    if sorted1 == sorted2:
        return True
    else:
        return False
    
def find_missing_num(input_list):
    input_list.sort()
    for i in range(len(input_list) - 1):
        if input_list[i] != input_list[i + 1] - 1:
            return input_list[i] + 1
    if input_list[1] != 1:
        return 1
    if input_list[-1] != 100:
        return 100
    return 0

numbers1 = []
for i in range(1,38):
    numbers1.append(i)
for i in range (39, 101):
    numbers1.append(i)  

numbers2 = []
for i in range(1,64):
    numbers2.append(i)
for i in range (65, 101):
    numbers2.append(i)  

# Programming Task #1: is_anagram()
print("Anagram Check for [arnab] and [banra]: ", is_anagram("arnab", "banra"))
print("Anagram Check for [iamlordvoldemort] and [tommarvoloriddle]: ", is_anagram("iamlordvoldemort", "tommarvoloriddle"))
print("Anagram Check for [task] and [jack]", is_anagram("task", "jack"))

print("")

# Programming Task #2: find_missing_num()
print(find_missing_num(numbers1))
print(find_missing_num(numbers2))

print("")


# Programming Task #3: student
kid = student.Student("Arnab Karmokar")
print(kid.name)

print("")

kid.add_grade("Advanced Topics in Math", 3.5)
kid.add_grade("Advanced Topics in Math", 3.5)
kid.add_grade("Advanced Topics in Math", 4.0)
kid.add_grade("Advanced Topics in Math", 2.5)
kid.add_grade("Advanced Topics in Math", 3.5)
kid.add_grade("Advanced Topics in Math", 4.0)
print(kid.grades)
print("Average for Advanced Topics in Math: ", kid.get_average("Advanced Topics in Math"))

print("")

kid.add_grade("AP English Language", 3.0)
kid.add_grade("AP English Language", 3.0)
kid.add_grade("AP English Language", 4.0)
kid.add_grade("AP English Language", 3.5)
kid.add_grade("AP English Language", 4.0)
kid.add_grade("AP English Language", 3.5)
print("Average for AP English Language", kid.get_average("AP English Language"))

print("")

print("Overall Grade Average: ", kid.get_overall_average())
print("Highest Grade: ", kid.highest_grade())
kid.visualize_grades()