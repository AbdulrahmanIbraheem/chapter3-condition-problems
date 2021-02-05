 
# 5. Mass and Weight
# Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
# the amount of mass of an object in kilograms, you can calculate its weight in newtons with
# the following formula:
# weight 5 mass 3 9.8
# Write a program that asks the user to enter an object’s mass, then calculates its weight. If
# the object weighs more than 500 newtons, display a message indicating that it is too heavy.
# If the object weighs less than 100 newtons, display a message indicating that it is too light.


# the mass object in kg entered by the user

mass_object_in_kg = float( input('enter the mass object in kg '.title() ).strip() )

# convert the mass object into newton

weight_object_in_newton = mass_object_in_kg * 3.98


if weight_object_in_newton > 500:
  print('the mass object is to havey!'.title())

else:
  print('the mass object is to light!'.title() )
