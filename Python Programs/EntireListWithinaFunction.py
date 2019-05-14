"""
0.initial setup:
a.create a variable and assign it a list of all integers
1.printing a list's elements using a for loop in a function:
a.create a function that will take a list as its input and prints that list's elements using a for loop
b.call the function you created in step 1.a. with the list you created in step 0.a. as its input.
2.generating lists using range():
a.use range() to generate a list that starts at 0 and ends at and includes 9 (range should only have 1 input.)
Assign
 this range() to a variable
b.use range () to generate a list that starts at 4 and ends at and includes 7 (range should only have 2 inputs.)
Assign
 this range() to a variable
c.use range to generate a list that starts at 5, increments up in steps of 5, and ends at and includes 20 (range
should
 have 3 inputs.) Assign this range() to a variable.
3.passing a list made using a range into a function:
a.create a function that takes and returns 1 input
b.print a call of the function you created in step 3.a. with the range you made in step 2.a. as its input
4.iterating through a list using range() and a for loop:
a.create a function that uses a for loop and a range (as was shown in the lecture video) to print all of the
elements
 from a list.
b.call the function you created in step 4.a. with the range you made in step 2.b. as its input.
5.modifying elements from a list using range:
a.Create a function that uses a for loop and a range() to iterate through and add 3 to each of the elements
from a list.
 The function should print the modified list.
b.call the function you created in step 5.a. with the list you made in step 0.a. as its input.
6.passing multiple lists into a function:
a.Create a function that takes and prints 2 inputs.
b.Call the function you created in step 6.a. with the list you modified in step 5.b. and the range() you made in
step
 2.c.
7.Iterating through a list of lists using a function:
a.Create a list that contains 3 lists. Each of those lists should be composed of all strings.
b.Create a function that appends all of the strings from the list you made in step a into a new, single list.
(This
 function should use 2 for loops.) This function should print the new list.
c.Call the function you made in step 7.b. using the list you created in step 7.a. as its input.
"""

list1=[1,2,3,4]
#1
def listprint(li):
 for ele in li:
     print(ele)

listprint(list1)

print("++++++++++++++++++++++++++++")

#2
rangelist1 = range(10)#[0,1,2,3,4,5,6,7,8,9]
rangelist2 = range(4,8)#[4,5,6,7]
rangelist3 = range(5,21,5)#[5,10,15,20]


#3
def range1fun(a):
 return a

print(range1fun(rangelist1))

print("++++++++++++++++++++++++++++")

#4
def range2fun(a):
 for ele in range(0,len(a)):
  print(a[ele])

range2fun(rangelist2)

print("++++++++++++++++++++++++++++")

def range3fun(a):
 for ele in range(0,len(a)):
  a[ele]+=3
  return(a)

print(range3fun(list1))

print("++++++++++++++++++++++++++++")

def multilist(a,b):
 print(a,b)

multilist(range3fun(list1),rangelist3) # you are a genius!!!!<3 love you!!!

print("++++++++++++++++++++++++++++")

lista=[["cat","bat"],["goat","sheep"],["aligator","frog"]]

def listInList(a):
 newbox = []
 for item in a:
  for element in item:
   newbox.append(element)

   print(newbox)

listInList(lista)

print("+++++++++++++")
all_strings = [["apple", "pear"], ["broccoli", "carrots", "corn"], ["pork", "beef"]]
# 7.b.
def concatenator(list_of_strings):
 new_list = []
 for index in range(0, len(list_of_strings)):
  for strings in list_of_strings[index]:
   new_list.append(strings)
  print(new_list)
# 7.c
concatenator(all_strings)

print("++++++++++++++++++")
def range3fun(a):
 for ele in range(0,len(a)):
  a[ele]+=3
  return(a)

print(range3fun(list1))

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4444")

int4=[1,2,4,5]

def fun11(a):
 for ele in a:
  print(ele)

fun11(int4)

listone = range(3)
listtwo = range(2,5)
listthree = range(2,13,5)

def flowerlist(a,b,c):
 newbox=[]
 for ele in range(0,len(a)):
  newbox.append(a[ele] + b[ele] + c[ele])
 return newbox

def iterationlist(a):
 for item in a:
  for element in item:
   print(element)

iterationlist([[1,2],[0,1],[3,4]])

fun11(int4)

print(flowerlist(listone,listtwo,listthree))