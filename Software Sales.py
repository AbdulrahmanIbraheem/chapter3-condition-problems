
product_price = 99
amount_purchased  = int( input("enter the amount purchased? ").strip() )

if amount_purchased >= 10 and amount_purchased <= 19:

  discount = product_price * 0.1
  price = product_price - discount
  payment = price * amount_purchased
 

elif amount_purchased > 2 and amount_purchased <= 49:

  discount = product_price * 0.2
  price = product_price - discount
  payment = price * amount_purchased
 
elif amount_purchased >= 50 and amount_purchased <= 99:

  discount = product_price * 0.3
  price = product_price - discount
  payment = price * amount_purchased

else:

  discount = product_price * 0.4
  price = product_price - discount
  payment = price * amount_purchased



print(f"the price befor the discount is ${product_price}\nthe discount amount is ${discount}\nthe price afer the discount is ${price}\nthe total purchase ${payment:.2f}")

