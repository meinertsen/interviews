# Write a function that returns all fibonacci numbers up to s

def fibo(s):	
    i = [0, 1]
    while sum(i[-2:]) <= s: i.append(sum(i[-2:]))
    return i

fibo(1000) # Generate Fibonacci sequence up to 1000

Out[]: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
