
price = 99

# amout of package purchased

amount_of_package_purchased = int( input('enter the amount of package purchased '.title()).strip() )


# conditions 

if amount_of_package_purchased >= 10 and amount_of_package_purchased <= 19:

  discount = price * 0.1

  print(f'the real price is ${price}. the discount is ${discount} the cost after the discount is ${price - discount}'.title())


elif amount_of_package_purchased >= 20 and amount_of_package_purchased <= 49:

  discount = price * 0.2

  print(f'the real price is ${price}. the discount is ${discount} the cost after the discount is ${price - discount}'.title())

elif amount_of_package_purchased >= 50 and amount_of_package_purchased <= 99:

  discount = price * 0.3

  print(f'the real price is ${price}. the discount is ${discount} the cost after the discount is ${price - discount}'.title())

else:

  discount = price * 0.4

  print(f'the real price is ${price}. the discount is ${discount} the cost after the discount is ${price - discount}'.title())
