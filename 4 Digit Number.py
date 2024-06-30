'''
Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.
1.Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
2.Наименьшая из полученных трёх сумм удаляется.
3.Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
Пример. Исходное число: 1982. Суммы: 1+9=10, 9+8=17, 8+2=10. Удаляется 10. Результат: 1017.
Укажите наибольшее число, при обработке которого автомат выдаёт результат 1315.
Примечание. Если меньшие из сумм равны, то отбрасывают одну из них.
'''

'''
The machine receives a four-digit number as input (the number cannot start with zero). Based on this number, a new number is constructed according to the following rules.
1. The first and second, second and third, third and fourth digits of a given number are added separately.
2. The smallest of the three amounts received is removed.
3. The remaining two amounts are written one after another in non-decreasing order without separators.
Example. Original number: 1982. Sums: 1 + 9 = 10, 9 + 8 = 17, 8 + 2 = 10. Remove 10. Result: 1017.
Specify the largest number that, when processed, the machine produces the result 1315.
Note. If the smaller sums are equal, then one of them is discarded.
'''

for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) + int(s[1])  # Adding First Two Digits
    k2 = int(s[1]) + int(s[2])  # Adding Next Two Digits
    k3 = int(s[2]) + int(s[3])  # Adding Last Two Digits
    first = max(k1, k2, k3)  # Picking The Highest Number
    second = k1 + k2 + k3 - first - min(k1, k2, k3)  # Picking The Second-Highest Number
    final = str(second) + str(first)  # Making The Final String
    if (final == '1315'): # Comparing
        print(i)
