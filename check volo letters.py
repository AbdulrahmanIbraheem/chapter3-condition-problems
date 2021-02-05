

letter = input("enter the letter ".capitalize() ).strip().lower()


if any([letter == 'o', letter == 'u', letter == "e", letter == "i", letter == "a"]):

  print(f"the letter [ {letter} ] is vowel letter ".capitalize() )

else:

  print(f"the letter {letter} is consonant.".capitalize() )

