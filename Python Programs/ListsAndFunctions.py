#Using Functions With Lists Problems:
"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable

1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input

2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input

3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
 result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.

4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
 .index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""

intList = [4,3,2,1]
strList = ["four","three","two","one"]
floatList = [1.0,2.0,3.0,4.0]

#1
def pass_list(li):
 return li

print(pass_list(intList))
print(pass_list(strList))
print(pass_list(floatList))

#2
def li_ele_access(li):
 return li[2]

print(li_ele_access(intList))
print(li_ele_access(strList))
print(li_ele_access(floatList))

#3
def list_modify(li):
 """
 empty=[]
 for ele in li:
  empty.append(ele*ele)
 print(empty)

list_modify(intList)
"""
 return (li[0]*li[1]*li[2]*li[3])

print(list_modify(intList))

#4
def concat_strList(li):
 holder=""
 for ele in li:
  holder+=ele
 print(holder)

concat_strList(strList)

def quo(li):
 print(li[2]/li[3])

quo(floatList)

def list_manip(li):
 li.append(7)
 li.remove(1)
 li.insert(3,0)
 li.pop(2)
 print(li)

list_manip(intList)

print("__________+_++++++++++++++++++++++++++++++++++++_+_______________________")

stringlist=["tokyo","osaka","chiba"]
def onefun(li):
 print(li[1])

def concat(li):
 print(li[2]+"frog")

def remov(li):
 li.remove("tokyo")
 print(li)

onefun(stringlist)
concat(stringlist)
remov(stringlist)

"""
def onefun(li):
 print(li[1])
 print(li[2]+"frog")
 li.remove("tokyo")
 print(li)

onefun(stringlist)
"""


