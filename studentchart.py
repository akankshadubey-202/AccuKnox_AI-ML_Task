import requests
import matplotlib.pyplot as plt

# API URL
api = 'https://mocki.io/v1/ae23e0ac-2091-44d8-b5e9-796bf217f1a4'

try:
    response = requests.get(api)
    data = response.json()
    students = data['students']
except Exception as e:
    print(f"Error fetching data from the API: {e}")
    students = []

exam = []
quiz = []
homework = []
for student in students:
    scores = student['scores']
    e_total = 0
    q_total = 0
    h_total = 0
    e_count = 0
    q_count = 0
    h_count = 0

    for score in scores:
        score_value = score['score']
        score_type = score['type']

        if score_type == 'exam':
            e_total += score_value
            e_count += 1
        elif score_type == 'quiz':
            q_total += score_value
            q_count += 1
        elif score_type == 'homework':
            h_total += score_value
            h_count += 1

    if e_count > 0:
        exam.append(e_total / e_count)
    if q_count > 0:
        quiz.append(q_total / q_count)
    if h_count > 0:
        homework.append(h_total / h_count)
# bar graph plot
categories = ['Exam', 'Quiz', 'Homework']
average_scores = [sum(exam) / len(exam), sum(quiz) / len(quiz), sum(homework) / len(homework)]

plt.bar(categories, average_scores, color=['pink', 'green', 'orange'])
plt.xlabel('Test Type')
plt.ylabel('Average Score')
plt.title('Average Test Scores by Type')
plt.ylim(0, 100)  # Set the y-axis limit
plt.show()
