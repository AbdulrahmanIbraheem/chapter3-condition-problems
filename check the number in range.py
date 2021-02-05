 
# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number. If the number is
# outside the range of 1 through 10, the program should display an error message. The following table shows the Roman numerals for the numbers 1 through 10:


# this user input in decimal number in range 1 to 10

userDecimal = int( input('enter a decimal number in ange of 1, 10: '.title()).strip() )


if userDecimal in range(1,10):

  if userDecimal == 1:

    print(f'\nthe number {userDecimal} in roman number is [ I ] '.title())

  elif userDecimal == 2:

    print(f'the number {userDecimal} is roman number is [ II ] ')

  elif userDecimal == 3:

    print(f'the number {userDecimal} is roman number is [ III ] ')

  elif userDecimal == 4:

    print(f'the number {userDecimal} is roman number is [ IV ] ')

  elif userDecimal == 5:

    print(f'the number {userDecimal} is roman number is [ V ] ')
  

  elif userDecimal == 6:

    print(f'the number {userDecimal} is roman number is [ VI ] ')

  elif userDecimal == 7:

    print(f'the number {userDecimal} is roman number is [ VII ] ')

  elif userDecimal == 8:

    print(f'the number {userDecimal} is roman number is [ VIII ] ')

  elif userDecimal == 9:

    print(f'the number {userDecimal} is roman number is [ IX  ] ')

  else :
    print(f'the number {userDecimal} is roman number is [ X ] ')
  
else:
   
   print('error, the vlue you entered is out of range try. try again later'.title())


