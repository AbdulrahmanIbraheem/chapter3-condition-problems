
# shippig charge 


weight_in_pounds = float( input('enter the amount of weight you want to ship '.title() ).strip() )



if weight_in_pounds <= 2 and weight_in_pounds > 0:

  print('the shipping price is $ 1.5 '.title() )

elif weight_in_pounds <= 6 and weight_in_pounds > 2:

  print('the shipping price is $ 3'.title() )

elif weight_in_pounds <= 10 and weight_in_pounds > 6:

  print('the shipping price is $ 4'.title() )

else:

  print('the shippig price is $ 4.75'.title() )
