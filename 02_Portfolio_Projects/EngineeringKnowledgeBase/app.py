import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("===== ENGINEERING KNOWLEDGE BASE =====")

current_folder = os.path.dirname(__file__)
notes_path = os.path.join(current_folder, "materials_notes.txt")

with open(notes_path, "r") as file:
    notes = file.read()

question = input("\nAsk a question about your notes: ")

response = client.responses.create(
    model="gpt-4.1-nano",
    input=f"""
You are an engineering study assistant.

Use ONLY the notes below to answer the question.

If the notes contain the topic or enough related information, answer using the notes.

Only say "I could not find that in the provided notes." if the topic is completely missing.

Do not use tables.
Use plain text only.
Keep the answer practical and clear.

NOTES:
{notes}

QUESTION:
{question}
"""
)

print()
print("=" * 60)
print("ANSWER FROM NOTES")
print("=" * 60)
print(response.output_text)
print("=" * 60)