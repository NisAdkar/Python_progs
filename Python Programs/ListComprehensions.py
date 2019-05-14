"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]

2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""


listc1 = [ele for ele in range(8,-1,-2)]
print(listc1)

listc2 = [ele*ele for ele in range(1,5)]
print(listc2)

listc3 = [ele*ele-1 for ele in range(5,8)]
print(listc3)

listc4 = [ele for ele in range(2,10) if ele!=5 and ele!=6]
print(listc4)

listc5 = [ele for ele in range(10,0,-1) if ele>7 or ele<4]
print(listc5)

listc6 = [ele for ele in range(1,11) if ele != 2 and ele != 3 and ele != 7 and ele !=8]
print(listc6)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

lista = [a for a in range(1,10,2)]
print(lista)

listb = [a for a in range(3,8)]
print(listb)

listc = [a for a in range(1,10)if a%2!=0]
print(listc)

listd = [a for a in range(1,8,1)if a>2]
print(listd)