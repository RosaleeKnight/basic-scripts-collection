def exam_grade(score):
	if score >= 90:
		grade = "Top Score"
	elif score >= 70:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(75))