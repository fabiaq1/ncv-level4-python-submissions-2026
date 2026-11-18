import random


def generate_marks(count, low, high):
    marks = []
    for i in range(count):
        marks.append(random.randint(low, high))
    return marks

random.seed(2026)
print(generate_marks(8, 30, 100))
