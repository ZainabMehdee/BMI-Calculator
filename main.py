print('\n\t\t\tThe BMI Calculator')
print('\n\n Welcome to this BMI Calculator! You can check if you are healthy!')

user_input = input(' Type either "metric" or "imperial" for your preferred units\n or press "Enter" to Exit: ')

while user_input == 'metric':
    height = float(input('Enter your height in meters: '))
    weight = int(input('Enter your weight in kg: '))
    bmi = round(weight/ height**2 , 2)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'You are underweight. You should increase your food intake.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,"Congrats! You are healthy!")

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'Sadly, you are overweight. Please take care of your health.')

    elif bmi > 30:
        print('Your BMI is', bmi,'You are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

while user_input == 'imperial':
    height = int(input('Enter your height in inches: '))
    weight = int(input('Enter your weight in pounds: '))
    bmi = round((weight*703)/(height*height, 2))

    if bmi <= 18.5:
        print('Your BMI is', bmi,'You are underweight. You should increase your food intake.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'Congrats! You are healthy!')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'Sadly, you are overweight. Please take care of your health.')

    elif bmi > 30:
        print('Your BMI is', bmi,'You are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

input('\n\n Press enter to exit. Bye~ :}.')

