# 1

# class Soda:
#     def __init__(self, initialize):
#         if isinstance(initialize,str):
#             self.initialize = initialize
#         else:
#             self.initialize = None
#     def show_my_drink(self):
#         if self.initialize:
#             print(f'Газировка и {self.initialize}')
#         else:
#             print('Обычная газировка')

# first = Soda('Pepsi')
# first.show_my_drink()

# --------------------------------------

# 2

# class trainglechecker():
#     def __init__(self, a, b, c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def is_traingle(self):
#         if self.a and self.b and self.c >=1:
#             if (self.a+self.b>self.c) and (self.a+self.c>self.b) and (self.c+self.b>self.a):
#                 return f'Ура, можно построить треугольник!'
#             else:
#                 return f' Жаль, но из этого треугольник не сделать'
#         else:
#             return f' С отрицательными числами ничего не выйдет!'
    
# first = trainglechecker(1,5,1)
# print(first.is_traingle())


# ------------------------------------------

# 3

# class Universal:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def perimetr(self):
#         return (self.a+self.b)*2
    
# class rectangle(Universal):
#     def perimetr(self):
#         return (self.a+self.b)*2

# first = Universal(1,1)
# print(first.perimetr())

# second = rectangle(1,2)
# print(second.perimetr())