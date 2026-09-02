marks = {
    "Arun": 75,
    "Bala": 90,
    "Kiran": 60,
    "David": 85
}

average = sum(marks.values()) / len(marks)

print("Average:", average)

for name, mark in marks.items():
    if mark > average:
        print(name, mark)