# Subset pair sum question: https://www.youtube.com/watch?v=XKu_SEDAykw

# python solution for unsorted numbers using a list comprehension with if else

a = [1, 2, 3, 9]
b = [1, 2, 4, 4, 9, 6] # extended from youtube example to illustrate unsorted sequence
s = 8

# Are the numbers sorted: no
# integers, negatives: assume integers which can be negative

# Two For loops, Qudratic
# Binary search
# Pair wise sums, the smallest pair, the largest pair

def test(numbers,s):
    comps,pairs=[],[]
    [comps.append(s-i) if i not in comps else pairs.append((s-i,i)) for i in numbers]
    return {True: pairs} if pairs else False # List of tuples in a dictionary

test(a,s)
test(b,s)
