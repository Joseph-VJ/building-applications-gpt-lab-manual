# ---- Common Helper Program (from ollama_helper.py) ----
import requests

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
print("AI BLOG CONTENT GENERATOR")

topic = input("Enter blog topic: ")
style = input("Enter writing style (Formal/Casual/Informative): ")

prompt = f"""
Write a blog on the topic: {topic}.
Use this writing style: {style}.

Include:
1. An attractive title
2. Introduction
3. Main content with headings
4. Conclusion
"""

blog = ask_ollama(prompt)

print("\nGENERATED BLOG\n")
print(blog)

with open("blog.txt", "w", encoding="utf-8") as file:
    file.write(blog)

print("\nBlog saved as blog.txt")
