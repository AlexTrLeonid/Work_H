# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

n = input('Введите билет с шестизначным номером: ')
m = int(n[0]) + int(n[1]) + int(n[2])
r = int(n[3]) + int(n[4]) + int(n[5])
if m == r:
    print('Yes')
else:
    print('NO')
