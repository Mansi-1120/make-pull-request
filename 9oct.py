# Python code to find GCD of factorials oftwo numbers. 


import math 

  def gcdOfFactorial(m, n) : 

    return math.factorial(min(m, n)) 

  
# Driver code 

m = 5

n = 120

print(gcdOfFactorial(m, n)) 
