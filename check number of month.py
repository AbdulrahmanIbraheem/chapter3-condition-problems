
# this program will ask the user to enter the number of month between 1, 12
# if the it is between 1, 3 it display the month in the first quarter
# if the number between 4,6 display the month in the second quarter
# if the number between 7,9 display the month in the third quarter
# if the number  between 10, 12 display month in the fourth quarter

# note and display the name of the month

# user input [ number of the month ] between 1, 12

numberOfTheMonthe = int(input('enter the number of month between 1, 12 '.title() ).strip() )

if any([numberOfTheMonthe == 1, numberOfTheMonthe == 2, numberOfTheMonthe == 3]):

    if numberOfTheMonthe == 1:

      print(f'the montn {numberOfTheMonthe} is january and it is in the first quarter of the year'.title())

    elif numberOfTheMonthe == 2:

      print(f'the month {numberOfTheMonthe} is fetruary and it is in the first quarter of the year '.title() )

    else:
      
      print(f'the month {numberOfTheMonthe} is march and it is in the first quarter of the year '.title()) 

elif any([numberOfTheMonthe == 4, numberOfTheMonthe == 5, numberOfTheMonthe == 6]):

    if numberOfTheMonthe == 4:

      print(f'the month {numberOfTheMonthe} is april and it is in the second quarter of the year '.title() )

    elif numberOfTheMonthe == 5:

      print(f'the month {numberOfTheMonthe} is may and it is in the second quarter of the year '.title() ) 
    
    else:
      
      print(f'the month {numberOfTheMonthe} is june and it is in the second quarter of the year '.title() )

  
elif any([numberOfTheMonthe == 7, numberOfTheMonthe == 8, numberOfTheMonthe == 9]):

    if numberOfTheMonthe == 7:

      print(f'the month {numberOfTheMonthe} is july and it is in the third quarter of the year '.title() )

    elif numberOfTheMonthe == 8:

      print(f'the month {numberOfTheMonthe} is august and it is in the third quarter of the year '.title() )

    else:

        print(f'the month {numberOfTheMonthe} is september and it is in the third quarter of the year '.title() )

elif any([numberOfTheMonthe == 10, numberOfTheMonthe == 11, numberOfTheMonthe ==12]):

  if numberOfTheMonthe == 10:

    print(f'the month {numberOfTheMonthe} is october and it is in the fourth quarter of the year '.title() )

  elif numberOfTheMonthe == 11:

    print(f'the month {numberOfTheMonthe} is november and it is in the fourth quarter of the year '.title() )

  else:
    
    print(f'the month {numberOfTheMonthe} is decimber and it is in the fourth quarter of the year '.title() )

else:

    print('the month you enered is out of range....'.title() )

    
