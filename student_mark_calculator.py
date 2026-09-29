print("====================================")
print("       STUDENT MARK CALCULATOR")
print("====================================")

name = input("Enter student name: ")

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
python = int(input("Enter Python mark: "))
computer = int(input("Enter Computer mark: "))
accounts = int(input("Enter Accounts mark: "))

total = tamil + english + python + computer + accounts
average = total / 5

print("\n====================================")
print("             RESULT")
print("====================================")

print("Student Name :", name)
print("Tamil        :", tamil)
print("English      :", english)
print("Python       :", python)
print("Computer     :", computer)
print("Accoun…