quote = input("Enter your favorite quote:")

file = open("notes2.txt", "w")

file.write(quote)

file.close()

file = open("notes2.txt", "r")

content = file.read()

print(content)

file.close()