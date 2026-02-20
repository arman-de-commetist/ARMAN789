
# point = (10, 3)
# print[0] = 99 ошибка так делать нельзя

# student = {
#     "name": 'Ali',
#     "age": 16
# }

# print(student["name"])


# students = [
#     {"name": "Ali", "grades": [90,80,79]},
#     {"name": "Dana", "grades": [100, 95]}
# ]

# data = {
#     "age": [10,20,16,18,20],
#     "city": ["Almaty", "Astana", "Aktobe", "Shymkent"]
# }

# pandas DataFreme

# items = ["asdas@gmail.com", "bek@gmail.com", "hgdsm@gmail.com", "armanospanov99@gmail.com"]

# unique = set(items)
# duplicates_count = len(items) - len(unique)
# print("unique:", unique)
# print("duplicates:", duplicates_count)

# items = ["asdas@gmail.com", "bek@gmail.com", "hgdsm@gmail.com", "armanospanov99@gmail.com"]
# seen = set()
# dups = set()

# for i in items:
#     if i in seen:
#         dups.add(i)
#     else:
#         seen.add(i)
# print("unique:", seen)
# print("duplicates_count:", len(items) - len(seen))
# print("duplicates_count", dups)


# text = "AI is cool and AI is useful"
# words = text.lower().split()

# freq = {}
# for i in words:
#     freq[i] = freq.get(i,0) + 1

#     print("freq:", freq)


# products = [
#     {"title": "Iphone": "category":, "mobile":, "price":500000},
#     {"title": "samsung": "category":, "mobile":, "price":500000},
#     {"title": "Asus": "category":, "laptop":, "price":500000},
#     {"title": "Macbook": "category":, "laptop":, "price":500000},
#     {"title": "Ipad": "category":, "tablet":, "price":500000}
# ]

# froup = []
# for i in products:
#     cat = i["category"]

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def info(self):
#         print(f"Студент: {self.name}, Оценки: {self.grades}")

#     def avg(self):
#         return sum(self.grades) / len(self.grades)
    

# s1 = Student("Arman", [90, 80, 45])
# s2 = Student("Arlan", [100, 16, 43])

# print(s1.name)
# s1.info()
# print(s1.avg())
# print(s2.name)
# s2.info()
# print(s2.avg())



class TextDataset:
    """Хранит список строк."""
    def __init__(self, texts):
        if not isinstance(texts, list) or not all(isinstance(t, str) for t in texts):
            raise TypeError("texts должен быть list[str]")
        self.texts = texts

    def __iter__(self):
        return iter(self.texts)

    def __len__(self):
        return len(self.texts)


class Preprocessor:
    """lower + убрать лишние пробелы."""
    def process_text(self, text: str) -> str:
        return " ".join(text.lower().split())

    def transform(self, dataset: TextDataset) -> TextDataset:
        return TextDataset([self.process_text(t) for t in dataset])
    
class Analyzer:
    """Считает частоты слов (dict) и уникальные слова (set)."""
    def __init__(self):
        self.word_freq = {}     
        self.unique_words = set()  

    def _tokenize(self, text: str) -> list[str]:
        
        return text.split()

    def fit(self, dataset: TextDataset):
        self.word_freq.clear()
        self.unique_words.clear()

        for text in dataset:
            for word in self._tokenize(text):
                self.unique_words.add(word)
                self.word_freq[word] = self.word_freq.get(word, 0) + 1

        return self  

    def top_n(self, n: int):
        return sorted(self.word_freq.items(), key=lambda x: x[1], reverse=True)[:n]

    raw = TextDataset([
        " Привет Мир ",
        "Привеm, мир!",
        "Python Python Python"
    ])

prep = Preprocessor()
clean = prep.transform(raw)

an = Analyzer().fit(clean)

print("Очищенные тексты:", clean.texts)
print("Уникальные слова:", an.unique_words)
print("Частоты слов:", an.word_freq)
print("Топ-3:", an.top_n(3))