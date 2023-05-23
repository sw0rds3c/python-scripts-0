#Generating a Fibonacci sequence using simple recursion
def fibonacciGenerator(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return (fibonacciGenerator(num-2)+fibonacciGenerator(num-1)) #returns the sum of the two previous numbers
n=int(input("Please enter a value to generate a Fibonacci sequence from: "))
print("The Fibonacci sequence is: ")
for n in range(0, n):
  print(fibonacciGenerator(n))
