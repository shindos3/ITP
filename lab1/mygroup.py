groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [2, 4, 3]
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["Информатика", "ИС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Миронов",
        "exams": ["История", "КТП", "Философия"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Алексей",
        "surname": "Егоров",
        "exams": ["Философия", "Информатика", "Математика"],
        "marks": [4, 3, 3]
    }
]

def print_students(students, avg):
    mark_sum = 0
    count = 0
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        for mark in student["marks"]:
            mark_sum += mark
            count += 1
        mark_avg = mark_sum / count
        if (mark_avg > avg):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))

avg = float(input("Введите средний балл: "))
print_students(groupmates, avg)
