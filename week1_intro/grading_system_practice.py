# GRADING SYSTEM: PRACTICING BASIC SKILLS IN PYTHON
# A =>  89+
# B =>  79+
# C =>  69+
# D =>  59+
# F =>  58 and lower

score = 20

if 89 <= score < 100:
    print("You score grade is 'A', Congratulations!!")
elif 79 <= score < 89:
    print("You score grade is 'B', You did well!!")
elif 69 <= score < 79:
    print("You score grade is 'C', Keep it up!!")
elif 59 <= score < 69:
    print("You score grade is 'D', You can do better next time!!")
elif 0 <= score <= 58:
    print("You score grade is 'F'. You failed the course, Try again!!")
else:
    print("The score you entered is invalid/incorrect, Crosscheck!")