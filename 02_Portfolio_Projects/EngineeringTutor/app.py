import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("===== WPI ENGINEERING AI =====")

question = input("Ask a study question: ")

response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"""
You are a Mechanical Engineering tutor.

Do not use tables.
Do not use markdown tables.
Use plain text only.
Keep answers readable in a terminal.

Format answers exactly like this:

TOPIC:

EXPLANATION:

EQUATION:

VARIABLES:
- variable =
- variable =
- variable =

EXAMPLE:

Question:
{question}
"""
)

answer = response.output_text

print()
print("=" * 50)
print("AI ANSWER")
print("=" * 50)
print(answer)
print("=" * 50)