'''
The sequence of Fibonacci numbers is given by the recurrence relation:

F(1) = 1

F(2) = 1

F(n) = F(n–2) + F(n–1), for n >2, where n is a natural number.

What is the ninth number in the Fibonacci sequence?

Write down only a natural number in your answer.
'''

'''
def F(N):
    if N == 1 or N == 2:
        return 1
    if N>2:
        return (F(N-2) + F(N-1))

print(F(9))
'''

def F(n):
    if n==1 or n==2:
        return n
    if n>2 and n%2==0:
        return (3*n + F(n-3))//3
    if n>2 and n%2!=0:
        return (7*n + F(n-1) - F(n-2))//5

print(F(35))