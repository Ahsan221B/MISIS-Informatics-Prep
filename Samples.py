# Question 4
# ((x ∧ ¬y) → (¬z ∨ ¬w))∧((w→x) ∨ y)
'''
print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not (((x and not y) <= (not z or not w)) and ((w <= x) or y)):
                    print(w, x, y, z)
'''

# Question 8
'''
def giveNewNumber(n):
    binary = bin(n)[2:]
    s = str(binary)
    s += str(s.count("1") % 2)
    s += str(s.count("1") % 2)
    return int(s, 2)


largest = 0
for n in range (0,100):
    result = giveNewNumber(n)
    if(result <90 and result>largest):
        largest = result

print(largest)
'''

# Question 12
'''
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

num = ((36**8) + (6**20) - 12)
print(numberToBase(num, 6))
'''

# Question 13
'''
F(0) = 0;

F(n) = F(n / 2), если n > 0 и при этом n чётно;

F(n) = 1 + F(n − 1), если n нечётно.
'''

'''
def algo(n):
    if n == 0:
        return 0
    if n > 0 and n%2 == 0:
        return algo(n//2)
    if n%2 != 0:
        return 1 + algo(n-1)

n = 0
while(algo(n)!=11):
    n+=1
print(n)
'''

# Question 14
'''
F(1) = 1;
F(n) = F(n − 1) + n если n>1
'''

'''
def algo(n):
    if n==1:
        return 1
    if n>1:
        return algo(n-1) + n

print(algo(30))
'''

# Question 11
'''
for x in '0123456789ABCD':
    num = int('1'+x+'563', 14) + int('871' + x + '3', 14)
    if(num % 24 ==0):
        print (x, ": ", num // 24)
'''


# 16209020
# Q14

'''
import sys
sys.setrecursionlimit(10**6)

def F(n):
    if n < 11:
        return n
    else:
        return n + F(n - 1)


print(F(2024) - F(2021))
'''

# Q13
'''
def F(n):
    if n == 0:
        return 0
    if(n>0 and n%2==0):
        return F(n/2)
    if(n%2!=0):
        return 1 + F(n-1)

n = 0
while(F(n)!=12):
    n+=1

print (n)
'''

# Q12
'''
for x in '0123456789ABCDE':
    num = int('97968'+x+'15', 15) + int('7'+x+'233', 15)
    if(num% 14 == 0):
        print(x, ' ',num // 14)
'''

# Q11
'''
num = 4**2018 + 2**2017 - 5
binary = bin(num)[2:]
print (binary.count('1'))
'''


# Class on Saturday
'''
def F(n):
    if n == 0:
        return 0
    if n>0 and n%2 == 0:
        return F(n/2)
    if n%2 != 0:
        return 1 + F(n-1)

count = 0
for n in range(1, 1000):
    if(F(n) == 3):
        count+=1

print(count)
'''

'''
def F(n):
    if n<= 1:
        return 0
    if n>1 and n%2!=0:
        return F(n-1) + 3* (n**2)
    if n>1 and n%2==0:
        return n/2 + F(n-1) + 2

print (F(49))

#OTBET: 62820.0
'''

'''
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n-1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n-2)

print(F(26))

#OTBET 4122

'''

# 16232596
'''
# Q14
def F(n):
    if n > 1000000:
        return n
    if n <= 1000000:
        return n + F(2*n)


count = 0
G1000 = F(1000) / 1000
for n in range(1, 1000000):
    G = F(n) / n
    if(G == G1000):
        count += 1

print(count)
'''

'''
# Q13
def F(n):
    if(n <= 2):
        return 1
    else:
        return F(n-2) * n

print(F(7))
'''

'''
# Q12
for x in range(37):
    #n = int('123' + str(x), 37) + int('4' + str(x) + '59', 37)
    n = 1 * 37 ** 3 + 2 * 37 ** 2 + 3 * 37 ** 1 + x + 4 * 37 ** 3 + x * 37 ** 2 + 5 * 37 + 9
    if(n%36 == 0):
        print(n, ": ", n // 36)
'''

'''
# Q11
for A in range(10**6):
    for x in '012345678':
        M = int('842' + x + '5', 9)
        N = int('8' + x + '725', 9)
        if (M + A) % N == 0:
            print ("A: ", A)
            exit()
'''

'''
# Q7
dictionary = []
for n in range(100, 3000):
    binary = bin(n)[3:]
    num = n - int(binary, 2)
    if num not in dictionary:
        dictionary.append(num)
print(len(dictionary))
'''

'''
Q4
print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if((x or not z) and (x == (not w)) and (x<=y)):
                    print(w, x , y, z)
'''

'''
print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not((x and not y) or (y == z) or not w):
                    print(w, x , y, z)
'''

'''
print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((w <= (not x)) == (z <= y)) and (y or w):
                    if(y == 0):
                        print(w, x , y, z)
'''

'''
print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if not ((w <= ( y== z)) and ( y == (z <= x))):
                        print(w, x , y, z)
'''

for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])
    k2 = int(s[1]) + int(s[2])
    k3 = int(s[2]) + int(s[3])
    first = max(k1, k2, k3)
    second = k1 + k2 + k3 - first - min(k1, k2, k3)
    final = str(second)+ str(first)
    if(final == '1315'):
        print(i)