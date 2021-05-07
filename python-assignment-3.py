number = input("Please enter a number: ")
list = [2,3,4,5,6,7,8,9]
count = 0
if int(number) != 2 and int(number) != 5 and int(number) != 7 :
  for i in list:
    if int(number) != 1 and not int(number)%int(i) == 0:
      count +=1
      if count == 8:
        print("Number is a prime number")
    else: 
      print("Number is not a prime number")
      break
else:
  print("Number is a prime number")



