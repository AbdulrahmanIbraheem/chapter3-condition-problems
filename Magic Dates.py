 # 6. Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the
# month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit year. The program should then determine whether the month times the day equals the
# year. If so, it should display a message saying the date is magic. Otherwise, it should display
# a message saying the date is not magic.


# day enter by the user

day = int( input('enter the data of the day '.title() ).strip() )

# month enter by user

month = int( input('enter the month in number '.title() ).strip() )

# year enter by the user

year = int(input('enter the year in number [ 2 digits monluy ] '.title() ).strip() )

if day * month == year:

  print(f'the year {year} is a magic year'.title() )

else:

  print(f'the year {year} is not a magic year'.title() )

