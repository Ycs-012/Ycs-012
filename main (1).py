#write a program that determines wheather a year entered by the user is a leapyear or not using ifelif- else statements

# Get the year from the user
year = int(input("Enter a year:"))

# check if it's a leap year 
if(year % 4 == 0 and year % 100 != 0) or(year % 400 == 0):
  print(f"{year} is a leap year.")
else:
  print(f"{year}is not a leap year.")
  
