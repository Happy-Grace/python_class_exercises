# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message
# If the score is between 0.0 and 1.0, print a grade using the following table:
#  Score Grade
#    >= 0.9  A
#    >= 0.8  B
#    >= 0.7  C
#    >= 0.6  D
#    < 0.6  F

# score = float(input("Please, enter your score for grading: "))
# scoreGrade  = "F"
#
# if (score >= 0.9 and score <= 1.0):
#     scoreGrade  = "A"
# elif (score >= 0.8 and score < 0.9):
#     scoreGrade  = "B"
# elif (score >= 0.7 and score < 0.8):
#     scoreGrade  = "C"
# elif (score >= 0.6 and score < 0.7):
#     scoreGrade  = "D"
# elif (score < 0.6 and score >= 0):
#     scoreGrade  = "F"
# else:
#     scoreGrade = "Wrong Input"
#
# print(scoreGrade)



# Using the try...except

while (True):
    try:
        score = float(input("Please, enter your score for grading: "))
        scoreGrade = "F"

        if (score >= 0.9 and score <= 1.0):
            scoreGrade = "A"
        elif (score >= 0.8 and score < 0.9):
            scoreGrade = "B"
        elif (score >= 0.7 and score < 0.8):
            scoreGrade = "C"
        elif (score >= 0.6 and score < 0.7):
            scoreGrade = "D"
        elif (score < 0.6 and score >= 0):
            scoreGrade = "F"
        else:
            scoreGrade = "Bad Score"


        print(scoreGrade)

        break

    except ValueError:
        print("Enter between the range 0.0 to 1.0!")
        continue


