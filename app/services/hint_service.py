from app.services.gemini_service import model


def generate_hint(question, attempt, hint_level):
    prompt = f"""
You are a Leetcode Mentor.

Question:
{question}

Student Attempt:
{attempt}

Hint Level:
{hint_level}

Rules:

Level 1:
Very small hint

Level 2:
Slightly stronger hint

Level 3:
Mention algorithm

Level 4:
Mention data structure

Level 5:
Give full solution

Never jump levels.
"""

    response = model.generate_content(prompt)
    return response.text
