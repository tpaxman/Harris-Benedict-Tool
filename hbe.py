import sys

def main():
   acceptible_activities = {1, 2, 3, 4, 5}
   gender = input('Enter your gender(m or f): ')
   while(gender != 'm' and gender != 'f'):
      gender = input('Please enter m or f: ')
   height = float(input('Height in inches: '))
   weight = float(input('Weight in pounds: '))
   age = float(input('Age in years: '))

   if(gender == 'm'):
      bmr = 66
      bmr += (6.23 * weight)
      bmr += (12.7 * height)
      bmr -= (6.8 * age)
   else:
      bmr = 655
      bmr += (4.35 * weight)
      bmr += (4.7 * height)
      bmr -= (4.7 * age)

   print("Your BMR is " + str(bmr))

   activity = int(input("How active are you? 1 for sedentary, 2 for lightly active, 3 for moderately active, 4 for very active, and 5 for extremely active: "))
   while(activity not in acceptible_activities):
      activity = int(input("Please enter a number between 1 and 5: "))

   if activity == 1:
      total = bmr * 1.2

   elif activity == 2:
      total = bmr * 1.375

   elif activity == 3:
      total = bmr * 1.55

   elif activity == 4:
      total = bmr * 1.7

   elif activity == 5:
      total = bmr * 1.9

   print("You burn " + str(total) + " calories per day.")

if __name__ == '__main__':
   main()
