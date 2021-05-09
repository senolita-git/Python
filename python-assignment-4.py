fibonacci_number = [1]
a = 0
b = 1
for i in range(0,56):
  fib = a + b
  a = b
  b = fib
  fibonacci_number.append(fib)
  if fib == 55:
    print(fibonacci_number)
  




