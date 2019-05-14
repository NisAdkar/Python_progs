"""
Creating Dictionaries, Accessing by Key, Adding to Dictionaries, and Length of a Dictionary:
1.create a 3 key: value pair dictionary and assign it to a variable
2.access and print a value from the list in step 1 by key
3.add a fourth key: value pair to the dictionary from step 1
4.print the dictionary from step 3
5.print the length of the dictionary from step 3
"""
# ----------------------------------------------------------------------------------------------------------------------
dict1={10:"indiana",20:"dalas",30:"texes"}

print(dict1[10])

dict1[40]="kalob"

print(dict1)

print(len(dict1))

# ----------------------------------------------------------------------------------------------------------------------
"""
Reassignment by Key and Del:
1.create a 2 key: value pair dictionary and assign it to a variable
2.print the dictionary from step 1
3.reassign a key from the dictionary in step 1 a different value than its original value
4.print the dictionary from step 3
5.remove a key: value pair from the dictionary from step 3 using del
6.print the new dictionary
"""
# ----------------------------------------------------------------------------------------------------------------------
dict2={12:"tokyo",13:"sapporo"}
print(dict2)

dict2[13]="Hokkaido"
print(dict2)

del dict2[12]
print(dict2)

# ----------------------------------------------------------------------------------------------------------------------

print("________________________________________")

dicta={}

dicta[12]="twelve"
dicta[13]="thirteen"
dicta[14]="fourteen"

print(dicta)
print(len(dicta))

print(dicta[14])

dicta[13]="paris"
print(dicta)

del dicta[13]
print(dicta)
