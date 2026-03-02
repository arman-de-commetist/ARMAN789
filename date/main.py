# with open('thirdlesson/data/input.txt', "r" encoding='usf-8') as file:
#     nums = [int(line.strip()) for line in file]
#     print(txt)

# text = "python AI"
# exaple(text.upper())
# text = "Python AI"
# print(text.lower())


# with open("thirdlesson/data/input.txt", "a", encoding='utf-8') as f:
#     f.write("Nev action")


# with open("thirdlesson/data/input.txt", "r", encoding='utf-8') as f:
#     text = f.read()


# text = text.lower()
# text = " ".join(text.split())

# with open("thirdlesson/data/clean.txt", "w", encoding='utf-8') as f:
#     f.write(text)

# print("Готово!  Сохронено в clean.txt")


# counts = {}

# with open("thirdlesson/data/shop.txt", "r", encoding='utf-8') as f:
#     for line in f:
#         item = line.strip()
#         if item == "":
#             continue


#         if item not in counts:
#             counts[item] = 0
#         counts[item] += 1

# best_ltem = None
# best_count = -1

# for item, count in counts.items():
#     if count > best_count:
#         best_count = C
#         best_item = item

#     print("Частоты: ")
#     for item, count in counts.items():
#         print(f"{item}: {count}")

# class TextDataset:
#     def __init__(self, texts: list[str]): 
#         self.texts = texts


# students = [
#     {"name": "Diana", "age": 20, "grade": 90},
#     {"name": "Alex", "age": 22, "grade": 85},
# ]

# with open("thirdlesson/data/out_students.csv", "w", encoding='utf-8') as f:
#     fieldnames = ["name", "age", "grade"]
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(students)

import json
# with open("thirdlesson/data/profile.json", "r", encoding='utf-8') as f:
#     data = json.load(f)

# print(data)
# print(type(data))

# data = {
#     "course": "AI Python",
#     "lesson": 3,
#     "topics": ["file", "csv", "json"],
#     "students": 13
# }

# with open("thirdlesson/data/meta.json", "w", encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=1)


import json, csv

# students = []
# with open("thirdlesson/data/students.csv", "r", encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         row["age"] = int(row["age"])
#         row["grade"] = int(row["grade"])
#         students.append(row)

# count = len(students)

# total = 0 
# for s in students:
#     total += s ["grade"]

# avg_grade = total / count if count > 0 else 0

# report = {
#     "count": count,
#     "avg_grade": avg_grade,
#     "students": students,
# }
# with open("thirdlesson/data/students.json", "w", encoding='utf-8') as f:
#     json.dump(report, f, ensure_ascii=False, indent=1)

# print("Запушено!")
    

# import json
# stats = {}
# with open("thirdlesson/data/visits2.json", "r", encoding='utf-8') as f:
#     for  line in f:
#          line = line.strip()
#          if  not line:
#                 continue
         
#          parts = line.split(",")
#          name = parts[0].strip(1)



import numpy as np

arr = np.array([3, 6, 9, 12, 15])

print("Массив:", arr)
print("dtype:", arr.dtype)
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("size:", arr.size)


arr2 = np.array([1, 2, 3, 4, 5])

print("Сумма:", arr2)
print("dtype:" , arr2.dtype)

zeros = np.zeros((4, 3))
ones = np.ones((4, 3))
fives = np.full((4, 3), 5)

print("Нули:\n", zeros)
print("Единицы:\n", ones)
print("Пятёрки:\n", fives)

print("Количество элементов:", zeros.size)

arr_range = np.arange(0, 20, 2)
arr_linspace = np.linspace(0, 20 ,6)

print("arange:", arr_range)
print("linspace:", arr_linspace)

np.random.seed(42)

grades = np.random.randint(1, 11, 12)

print("оценки:", grades)
print("Минимум:", grades.min())
print("Максимум:", grades.max())

arr3 =np.array([10, 20, 30, 40 ,50 , 60, 70])
print("Первый:", arr3[0])
print("Последний:", arr3[-1])
print("Со 2 по 5:", arr3[1:5])
print("Каждый второй:", arr3[::2])
print("Последние три:", arr3[-3:])


