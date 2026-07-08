import subprocess
import os

BASE_DIR = os.path.dirname(__file__)
# Update these paths to match your project files
PROJECTS = {
    "1": {
        "name": "Engineering Tutor",
        "file": "EngineeringTutor/app.py"
    },
    "2": {
        "name": "Engineering Knowledge Base",
        "file": "EngineeringKnowledgeBase/app.py"
    },
    "3": {
        "name": "Semiconductor Interview Prep",
        "file": "SemiconductorInterviewPrep/app.py"
    },
    "4": {
    "name": "Farm Operations Manager",
    "file": "FarmOperationsManager/app.py"
    }
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def launch(file_path):
    full_path = os.path.join(BASE_DIR, file_path)

    try:
        subprocess.run(["py", "-3.13", full_path])
    except FileNotFoundError:
        print("\nError: Could not find:")
        print(full_path)

    input("\nPress Enter to return to the portal...")


while True:
    clear()

    print("=" * 38)
    print("      AI ENGINEERING PORTAL")
    print("=" * 38)
    print()

    for key, project in PROJECTS.items():
        print(f"{key}. {project['name']}")

    print("\n0. Exit")

    choice = input("\nChoose: ")

    if choice == "0":
        print("\nGoodbye!")
        break

    elif choice in PROJECTS:
        launch(PROJECTS[choice]["file"])

    else:
        print("\nInvalid selection.")
        input("Press Enter to continue...")
    