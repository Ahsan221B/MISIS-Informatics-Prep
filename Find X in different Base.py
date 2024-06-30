'''
В выражении 123x  base37 + 4x59  base37 x обозначает некоторую цифру из алфавита системы счисления c основанием   base37. Определите наименьшее значение x, при котором значение данного выражения кратно 36. Для найденного x вычислите частное от деления данного выражения на 36 и запишите его в ответе в десятичной системе счисления.

In the expression 123x base  base37  + 4x59   base37 x denotes a certain digit from the alphabet of the number system with base 37. Determine the smallest value of x at which the value of this expression is a multiple of 36. For the found x , calculate the quotient of dividing this expression by 36 and write it in the answer in the decimal number system.

for x in range(37):
    #n = int('123' + str(x), 37) + int('4' + str(x) + '59', 37)
    n = 1 * 37 ** 3 + 2 * 37 ** 2 + 3 * 37 ** 1 + x + 4 * 37 ** 3 + x * 37 ** 2 + 5 * 37 + 9
    if(n%36 == 0):
        print(n, ": ", n // 36)

'''

'''
В системе счисления с основанием p выполняется равенство zxyx4 + xy658  =  wzx73. 
Буквами x, y, z и w обозначены некоторые цифры из алфавита системы счисления с основанием p. 
Определите значение числа xyzwp и запишите это значение в десятичной системе счисления.

In the number system with base p, the equality zxyx4 + xy658 = wzx73 holds. The letters x , y , z and w 
indicate some numbers from the alphabet of the number system with base p . 
Determine the value of the number xyzw p and write this value in the decimal number system.
'''
for p in range(1,10):
    for x in range(1,p):
        for y in range (1,p):
            for z in range (1,p):
                for w in range(1,p):
                    t1 = z*p**4+x*p**3+y*p**2+x*p**1+4
                    t2 = x*p**4+y*p**3+6*p**2+5*p**1+8
                    t3 = w*p**4+z*p**3+x*p**2+7*p**1+3
                    if t1 + t2 == t3:
                        print(x*p**3+y*p**2+z*p**1+w*p**0)