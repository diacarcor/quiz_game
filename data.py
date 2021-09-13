import requests

parameters = {
    "amount": 10,
    "category": "22",
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]
# question_data = [
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Seoul is the capital of North Korea.", "correct_answer": "False",
#          "incorrect_answers": ["True"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "The surface area of Russia is slightly larger than that of the dwarf planet Pluto.",
#          "correct_answer": "True", "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Israel is 7 hours ahead of New York.", "correct_answer": "True",
#          "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "The Southeast Asian island of Borneo is politically divided among 3 countries.",
#          "correct_answer": "True", "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Gothenburg is the capital of Sweden.", "correct_answer": "False",
#          "incorrect_answers": ["True"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "There exists an island named 'Java'.",
#          "correct_answer": "True", "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Mongolia was a part of the now non-existent U.S.S.R.",
#          "correct_answer": "False", "incorrect_answers": ["True"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "You could walk from Norway to North Korea while only passing through Russia.",
#          "correct_answer": "True", "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Japan has left-hand side traffic.", "correct_answer": "True",
#          "incorrect_answers": ["False"]},
#         {"category": "Geography", "type": "boolean", "difficulty": "medium",
#          "question": "Norway has a larger land area than Sweden.",
#          "correct_answer": "False", "incorrect_answers": ["True"]}
# ]
