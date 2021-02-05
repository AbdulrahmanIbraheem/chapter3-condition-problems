# 1. Number Analyser
# this program print powsitve the user input is greater than 0, otherwase print 
# negative if the user input is less than zero  else print ;zero' if the user input is zero


# the user input 

userInput = float( input('enter a number '.title() ).strip().title() ) 

if userInput > 0:

  print(f'the number {userInput:.2f} is a possitive number.... '.title())

elif userInput < 0:
  
  print(f'the number {userInput:.2f} is a negative number.... '.title())

else:

  print(f'the number {userInput:.2f} is \"zero\".....'.title() )
