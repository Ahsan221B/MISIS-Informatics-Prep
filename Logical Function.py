'''
Логическая функция F задаётся выражением ((w → ¬x) ≡ (z → y)) ∧ (y ∨ w).
Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

В ответе напишите буквы x, y, z, w в том порядке, в котором идут соответствующие им столбцы
(сначала буква, соответствующая первому столбцу; затем буква, соответствующая второму столбцу, и т.д.).
Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.
Пример. Пусть задано выражение x → y, зависящее от двух переменных x и y, и фрагмент таблицы истинности:
'''

'''
The logical function F is given by the expression (( w → ¬ x ) ≡ ( z → y )) ∧ ( y ∨ w).
Given a partially filled fragment containing non-repeating rows of the truth table of function F.
Determine which column of the truth table corresponds to each of the variables x , y , z , w .

In your answer, write the letters x , y , z , w in the order in which the columns corresponding to them appear 
(first, the letter corresponding to the first column; then, the letter corresponding to the second column, etc.). 
Write the letters in your answer in a row; there is no need to put any separators between the letters.
'''

print("w x y z")
for w in range(0, 2):
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                if ((w <= (not x)) == (z <= y)) and (y or w):
                        print(w, x , y, z)