student_scores = [
    150,
    142,
    185,
    120,
    171,
    184,
    149,
    24,
    59,
    68
]

total_exam_score = sum(student_scores)
sum = 0


for score in student_scores:
    sum += score
    print(score)
print(f"Total: {total_exam_score}")

print(f"Total Sum: {sum}")

print(max(student_scores))