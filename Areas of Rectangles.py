# 2. Areas of Rectangles
# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.

# the length and width for the rectangular 1
print('*' * 60)
print('...length and wifth for rectangular 1...'.title().center(60,'#'))
print('*' * 60)

rectangler1Length = float( input('enter the length for the rectangular 1 '.title() ).strip() )
rectangler1Width = float( input('enter the width for the rectangulare 2 '.title() ).strip() )

# caculating the area for the rectangular 1

rectangular1Area = rectangler1Length * rectangler1Width
print('\n')

print('*' * 60)
print('...length and wifth for rectangular 1...'.title().center(60,'#'))
print('*' * 60)

# theis is aske the use to enter the length and width for rectangulare 2

rectangler2Length = float( input('enter the length for the rectangulare 2 '.title() ).strip() )
rectangler2Width = float( input('enter the width for the rectangulare 2 '.title() ).strip() )

# calculating the area for rectangulare 2

rectangular2Area = rectangler2Length * rectangler2Width

# to chech wich rectangulare area is greater than the oter or if they are having the same area

if rectangular1Area > rectangular2Area:
  print('\nthe area for the rectangulare 1 is greater than the area for the rectangulare 2'.title())


elif rectangular2Area > rectangular1Area:
    print('\nthe area for the rectangulare 2 is greater than the area for the rectangulae 2'.title())

else:
    print('\nthe reactangulare1 and the reactangulare 2 having the same areas....'.title() )
