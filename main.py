print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0 
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Your ticket price will be $5.")
  elif age <= 18:
    bill = 7
    print("Your ticket price will be $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free rinde on us!")  
  else:
    bill = 12
    print("Your ticket price will be $12.") 
  want_photo = input("Do you want to have photos taken? Y or N  ")

  if want_photo == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller to ride.")  