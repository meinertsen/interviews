
# As a list comprehension
fizzbuzz = [print(i,'fizzbuzz') if i % 5 == 0 and i % 3 == 0 else print(i, 'fizz') if i % 3 == 0 else print(i, 'buzz') if i % 5 == 0 else print(i) for i in range(1,21)]
"""
Out[]: 
1
2
3 fizz
4
5 buzz
6 fizz
7
8
9 fizz
10 buzz
11
12 fizz
13
14
15 fizzbuzz
16
17
18 fizz
19
20 buzz
"""
# As a function, returns list of tuples
def fizzbuzz(n):
    return ([(i,'fizzbuzz') if i % 5 == 0 and i % 3 == 0 
            else (i, ' fizz') if i % 3 == 0 
            else (i, 'buzz') if i % 5 == 0 
            else (i,) for i in range(1,n+1)])
fizzbuzz(20)
"""
Out[]: 
[(1,),
 (2,),
 (3, ' fizz'),
 (4,),
 (5, 'buzz'),
 (6, ' fizz'),
 (7,),
 (8,),
 (9, ' fizz'),
 (10, 'buzz'),
 (11,),
 (12, ' fizz'),
 (13,),
 (14,),
 (15, 'fizzbuzz'),
 (16,),
 (17,),
 (18, ' fizz'),
 (19,),
 (20, 'buzz')]
 """

