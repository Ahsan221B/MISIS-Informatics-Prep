'''
На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1.  Строится двоичная запись числа N.
2.  Далее эта запись обрабатывается по следующему правилу:
а)  если число чётное, то к двоичной записи числа слева дописывается 10;
б)  если число нечётное, то к двоичной записи числа слева дописывается 1 и справа дописывается 01.
Полученная таким образом запись является двоичной записью искомого числа R.
Например, для исходного числа 410  =  1002 результатом будет являться число 2010  =  101002, а для исходного числа 510  =  1012 результатом будет являться число 5310  =  1101012.
Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число R, большее, чем 441. В ответе запишите это число в десятичной системе счисления.
'''


'''
The input of the algorithm is a natural number N. The algorithm constructs a new number R from it as follows.
1. A binary representation of the number N is constructed .
2. This record is then processed according to the following rule:
a) if the number is even, then 10 is added to the left of the binary representation of the number;
b) if the number is odd, then 1 is added to the left of the binary notation of the number and 01 is added to the right.
The entry obtained in this way is a binary entry of the desired number R.
For example, for the original number 4 base10 = 100 base2 the result will be the number 20 base10 = 10100 base2 , and for the original number 5 base10 = 101 base2 the result will be the number 53 base10 = 110101 base2 .
Indicate the minimum number N , after processing which using this algorithm, a number R greater than 441 is obtained. In your answer, write this number in the decimal number system.
'''


def getR(N):
    binary = bin(N)[2:]
    if(N%2 == 0):
        binary = '10' + binary
    else:
        binary = '1' + binary + '01'
    return int(binary, 2)

for N in range(10**6):
    if(getR(N) > 441):
        print(N)
        exit()