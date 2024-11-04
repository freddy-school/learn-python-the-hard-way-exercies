from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, im the {script} script")
print("i will ask u some questons")
print(f"do you know me {user_name}")
know = input(prompt)

print(f"where do you live {user_name}")
lives = input(prompt)


print(f"so you know {know} me and u live in {lives}")
