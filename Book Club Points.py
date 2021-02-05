
# 11. Book Club Points
# Serendipity Booksellers has a book club that awards points to its customers based on the
# number of books purchased each month. The points are awarded as follows:
# š ,I D FXVWRPHU SXUFKDVHV  ERRNV KH RU VKH HDUQV  SRLQWV
# š If a customer purchases 2 books, he or she earns 5 points.
# š If a customer purchases 4 books, he or she earns 15 points.
# š If a customer purchases 6 books, he or she earns 30 points.
# š If a customer purchases 8 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.

# user amount of booking this month
costmuerBooks = int( input('enter the amount of booking you made this month '.title() ).strip() )

if costmuerBooks == 0:

  print(f'you purchased {costmuerBooks} book this month your poins is 0 points...'.title())

elif costmuerBooks == 2:

  print(f'you purchase {costmuerBooks} books this month your points are 5 points'.title())

elif costmuerBooks == 4:

  print(f'you purchase {costmuerBooks} books this month your points are 15 points'.title())



elif costmuerBooks == 6:

  print(f'you purchase {costmuerBooks} books this month your points are 30 points'.title())


else :

  if costmuerBooks >= 8:

    print(f'you purchase {costmuerBooks} books this month your points are 60 points'.title())


