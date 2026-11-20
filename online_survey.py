import csv
from datetime import datetime

print("===== ONLINE SURVEY SYSTEM =====")

name = input("Enter your name: ")

questions = [
    "How do you rate our service? (Good/Average/Poor): ",
    "Is our service easy to use? (Yes/No): ",
    "Would you recommend our service? (Yes/No): "
]

responses = []

for question in questions:
    answer = input(question)
    responses.append(answer)

with open("survey_responses.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        name,
        *responses,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

print("\n===== SURVEY SUBMITTED =====")
print("Thank you for your feedback!")

print("\nYour Responses:")
for i, answer in enumerate(responses, 1):
    print(f"Question {i}: {answer}")
