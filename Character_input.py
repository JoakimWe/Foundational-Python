import datetime as dt
name = input("What's your name?")
age = input("How old are you?")
year = dt.date.today().year
age_100 = (year - int(age)) + 100
print(name + " you will turn 100 years old in " + str(age_100))
