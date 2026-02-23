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
    

import json
stats = {}
with open("thirdlesson/data/visits2.json", "r", encoding='utf-8') as f:
    for  line in f:
         line = line.strip()
         if  not line:
                continue
         
         parts = line.split(",")
         name = parts[0].strip(1)


