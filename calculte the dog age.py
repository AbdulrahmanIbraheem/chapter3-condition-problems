
h_age = float( input("what is the dog age? ".capitalize() ).strip() )


if h_age <= 2:

  d_age = h_age * 10.5

  print(f"the dog's age is {d_age}")

else:
# else h_age > 2:

    d_age = 21 + (h_age - 2) * 4
    print(f"the dog age is {d_age}"
