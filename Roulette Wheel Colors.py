# 9. Roulette Wheel Colors
# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
# as follows:
# š 3RFNHW  LV JUHHQ
# š For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
# pockets are black.
# š For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
# pockets are red.
# š For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
# pockets are black.
# š For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
# pockets are red.
# Write a program that asks the user to enter a pocket number and displays whether the
# pocket is green, red, or black. The program should display an error message if the user
# enters a number that is outside the range of 0 through 36.


userNumber = int( input('enter a number between 0, 36: '.title() ).strip() ) 


if userNumber in range(0,36+1):

  if userNumber == 0:

    print('the color package is green...'.title())

  if userNumber in range(1,10+1):

    if userNumber % 2 != 0:

      print('the color package is red...'.title() )

    else:
      
      print('the color is package is black...'.title())

  elif userNumber in range(11,18+1):

    if userNumber % 2 != 0:

      print('the color package is black...'.title() )

    else:

      print('the color package is red...'.title() )

  elif userNumber in range(19,28+1):

    if userNumber % 2 != 0:

      print('the color package is red...'.title() )

    else:
      
      print('the color package is black...'.title())
  
  else:

    if userNumber in range(29,36+1):

      if userNumber % 2 != 0:

        print('the color package is black...'.title() )

      else:

        print('the color package is red...'.title() )

else:

  print('error, the value you entered is out of range....'.title())

