print("===== WPI AI STUDY ASSISTANT =====")

question = input("Ask a study question:")

print()
print("You asked:")
print(question)

print()
print("AI Answer:")

if "hooke" in question.lower():
    print("Hooke's Law states that force equals spring constant times displacement.")

elif "stress" in question.lower():
    print("Stress is force divided by area.")

elif "strain" in question.lower():
    print("Strain is deformation divided by original length.")

elif "torque" in question.lower():
    print("Torque equals force times distance from the pivot.")
    
else:
    print("I don't know that yet.")

