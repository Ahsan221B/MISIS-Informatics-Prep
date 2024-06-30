'''

Type 14 No. 27411
Значение выражения 49^7 + 7^21 − 7? записали в системе счисления с основанием 7.
Сколько цифр «6» содержится в этой записи?

The value of the expression 49^7 + 7^21 − 7? written in a base 7 number system.
How many digits "6" are there in this entry?


N = 49**7 + 7**21 - 7
s = ''
#Converting to base 7
while N!=0:
    s = s + str(N%7)
    N = N // 7
# Making the strong backwards
s = s[::-1]
# Counting how many digits are 6
print(s.count('6'))

'''

'''
Числа M и N записаны в системе счисления с основанием 9 соответственно.

M = 842x59, N = 8x7259

В записи чисел переменной x обозначена неизвестная цифра из алфавита девятеричной системы счисления. 
Определите наименьшее значение натурального числа A, при котором существует такой x, что M + A кратно N.
'''

for A in range(10**6):
    for x in '012345678':
        M = int('842' + x + '5', 9)
        N = int('8' + x + '725', 9)
        if (M + A) % N == 0:
            print ("A: ", A)
            exit()