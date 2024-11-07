grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # множество
students_ = (list(students))  # список
average_1 = sum(grades[0]) / len(grades[0])  # средний балл
average_2 = sum(grades[1]) / len(grades[1])
average_3 = sum(grades[2]) / len(grades[2])
average_4 = sum(grades[3]) / len(grades[3])
average_5 = sum(grades[4]) / len(grades[4])
dict_ = {'Aaron': average_1, 'Bilbo': average_2, 'Johnny': average_3, 'Khendrik': average_4, 'Steve': average_5, }
print('Средние баллы студентов: ', dict_)

