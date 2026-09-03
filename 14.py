marks = {
    "Arun": 75,
    "Bala": 90,
    "Kiran": 65,
    "David": 85
}

sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1]))

print(sorted_marks)