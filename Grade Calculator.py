 

# 7. Grade Calculator
# A class has two tests worth 25 points each along with a main exam worth 50 points. For a student to pass the class, they must obtain an overall score of at least 50 points, and must obtain at
# least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than
# 25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
# If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
# If they get less than 80 but more than 60, they get a “Credit” grade.
# If they get less than 60, they get a ”Pass” grade.
# Write a program that prompts the user to enter their points for both tests and the exam and
# converts the values to integers. The program should first check if the points entered for the
# tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam
# score is not between 0 and 50, the program should display an error message. Otherwise,
# the program should display the total points and the grade. 


# the score for the test1 and test2 

test1 = float( input('enter the scor for test 1 '.title() ).strip() ) 

# test 2
test2 = float( input('enter the scor for test 2 '.title() ).strip() ) 


# main exam or final exam

final_exam_score = float( input('enter your final exam scor '.title() ).strip() )


# caculating the average 

average = test1 + test2 + final_exam_score


# conditions

if all([test1 >= 12.5, test2 >= 12.5, final_exam_score >= 25]):

  if average >= 90:

    print(f'your average is {average} your  GPA is [ A ]')
  

  elif average >= 80: 

    print(f'your average grade is {average} and your GPA is [ A- ]')

  elif average >= 70:

    print(f'your average garde is {average} and your GPA is [ B ]')

  elif average >= 60:

    print(f'your average garde is {average} and your GPA is [ C ]')
 
  elif average >= 50:

    print(f'your average garde is {average} and your GPA is [ C- ]')

elif all([test1 < 12.5, test2 < 12.5, final_exam_score < 25]):


  # if all([test1 < 12.5, test2 < 12.5, final_exam_score < 25]):
  print('sorry, you fialed in all the tests including the final exam you need to re-study the subject.... '.title())

else: 
  
  if any([test1 < 12.5, test2 < 12.5, final_exam_score < 25]):

    if test1 < 12.5:

      print('you fialed in test 1 you need to re-do it again'.title())

    elif test2 < 12.5:

      print('you fialed in test 2 and you need to re-do it again'.title() )

    else:

      print('you fialed in the final exam you need to re-do it again'.title())
    

