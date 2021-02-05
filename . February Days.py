
year = float( input("enter the current year ".capitalize() ).strip() )

if year % 4 == 0 and not year % 100 == 0:

  print(f"in {year} the February has 29 days.")

else:
   
   print(f"in {year} February has 28 days.")
