listy=[1,2,3]
empty=[]

tup="just","do","it"
nike=""

for element in listy:
 empty.append(element*2)

for ele in tup:
 nike+=ele

print(empty)
print(nike)


"""
Tuples:
1.create a 4 element tuple that consists of a float, an integer, a Boolean value, and a string. Assingn this tuple to a
 variable
2.print the tuple from step 1
3.print the the second element from the tuple you made in step 1
4.print the first element from the tuple you made in step 1
5.slice and print the first 3 elements of the tuple from step 1
6.slice and print the last 3 elements of the tuple from step 1
7.slice and print the middle 2 elements of the tuple from step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
tup1= (4.0,4,True,"top")
print(tup1)

print(tup1[1])

print(tup1[0])

print(tup1[:3])

print(tup1[1:])

print(tup1[1:3])
# ----------------------------------------------------------------------------------------------------------------------
"""
For Loops:
1.create a variable and assign it the tuple ("Bohr", "Leibniz", "Einstein")
2.create a variable and assign it an empty list
3.create a variable and assign it the list [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
4.use a for loop to go through and print each of the elements from the tuple in step 1 individually
5.use a for loop and .append() to add the middle 6 elements to the empty list from step 2
6.print the new list
"""
# ----------------------------------------------------------------------------------------------------------------------
strtup=("Bohr", "Leibniz", "Einstein")
cty=[]
vallist=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for alpa in strtup:
 print(alpa)

for num in vallist:
 if num>1 and num<8:
  cty.append(num)

print(cty)
# ----------------------------------------------------------------------------------------------------------------------

print("---------------------------------------------------------------")

tupa=1,2,3,4

print(tupa[1])

print(tupa[:2])

print(tupa[1:3])

print(tupa[2:])

for tu in tupa:
 print(tu)