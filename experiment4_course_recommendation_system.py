# ---- Common Helper Program (from ollama_helper.py) ----
import requests
import csv

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()

    return response.json()["response"]

# ---- Experiment program ----
courses = []
with open("courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append(row)

print("PERSONALIZED COURSE RECOMMENDATION SYSTEM")

name = input("Enter student name: ")
interest = input("Enter your interest: ")
skill = input("Enter skill level (Beginner/Intermediate/Advanced): ")

prompt = f"""
You are a course recommendation assistant.

Student name: {name}
Student interest: {interest}
Student skill level: {skill}

Available courses:
{courses}

Recommend three suitable courses only from the available list.
Give a short reason for each recommendation.
Do not invent courses.
"""

result = ask_ollama(prompt)

print("\nRECOMMENDED COURSES\n")
print(result)
