
# BMI CACULATOR

# username 

userName = input('what is your name '.title()).strip()
# user enter his or her weigt in pounds

userWeight = float(input('enter you weight in kg '.title() ).strip() )


# user hight in inches
userHight = float( input('enter your hight in inches '.title() ).strip() )

BMI = userWeight / userHight ** 2

if BMI <= 18.5:

  print(f'hi, {userName} you are underweight' ) 

elif BMI > 18.5 and BMI < 24.5:

  print(f'hi {userName} your BMI is normal ')

else:

  print(f'hi, {userName} your  overweight...')

