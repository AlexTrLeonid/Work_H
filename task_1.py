# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

m = int(input('Введите трёхзначное число '))
print(m//100 + m//10%10 + m%10)

