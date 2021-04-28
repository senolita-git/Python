#covid19-if statements
age = input("Are you a cigarette addict older than 75 years old?")
age = age.title()
if age == "Yes":
  age = True
else:
    age = False
chronic = input("Do you have a severe chronic disease?")
chronic = chronic.title()
if chronic == "Yes":
  chronic = True
else:
    chronic = False
immune = input("Is your immune system too weak?")
immune = immune.title()
if immune == "Yes":
  immune = True
else:
    immune = False

if (age or chronic or immune) == True:
  print("You are in risky group")
else:
  print("You are not in risky group")

