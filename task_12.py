# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def Num(A,B):
     if B == 0:
        return 1
     return A**B
     
     
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print(Num(A,B))