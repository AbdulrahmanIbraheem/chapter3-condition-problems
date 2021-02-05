  

# user enter the amount of money in cent like one cent 2 cent ...
userpennies = float( input('enter the amount of pennies '.title() ).strip() )


# the amount of money in the type of 5 cent
useNrnickels = float( input('enter the amount of nrnickets '.title() ).strip() )

# the amount of money in type of 10 cents
useDimes = float( input('enter the amount of money in dimes type '.title() ).strip() ) 


# the amount of money in the type of quarters
userQuarters = float( input('enter the amount of money in the type of quarters '.title() ).strip() )


totalMoneyInDollar = ((userpennies * 1 ) + (useNrnickels * 5) + (useDimes * 10)  + (userQuarters * 25)) / 100


if totalMoneyInDollar == 1 :
  print('congritulation, you won!...'.title() )

else:

  print('the amount you entered is maybe less or more than one dollar...'.title())
