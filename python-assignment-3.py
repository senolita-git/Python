number = input("Please enter a number: ")
count = 0
for i in range(1,int(number)+1):
  if int(number)%i == 0:
    count += 1
if count >= 3 or int(number) == 1 or int(number) == 0:
      print("The number is not a prime number")
else:
      print("The number is a prime number")
      
  



