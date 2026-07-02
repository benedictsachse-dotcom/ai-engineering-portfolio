import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("===== SEMICONDUCTOR INTERVIEW PREP AI =====")
print("1. Equipment Engineer")
print("2. Process Engineer")
print("3. Mechanical Engineering Intern")
print("4. Semiconductor Basics")

choice = input("Choose a role: ")

if choice == "1":
    role = "Equipment Engineer"
elif choice == "2":
    role = "Process Engineer"
elif choice == "3":
    role = "Mechanical Engineering Intern"
elif choice == "4":
    role = "Semiconductor Basics"
else:
    role = "General Semiconductor Intern"

response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"""
You are a semiconductor engineering interview coach.

The user is a Mechanical Engineering student at WPI interested in TSMC, ASML, and Lam Research.

Create interview prep for this role:
{role}

Format in plain text only. No tables.

Include:
1. Five likely interview questions
2. Short model answer for each
3. Key concepts to study
4. One mini quiz with answers

Keep it practical and beginner-friendly.
"""
)

print()
print("=" * 60)
print("INTERVIEW PREP")
print("=" * 60)
print(response.output_text)
print("=" * 60)