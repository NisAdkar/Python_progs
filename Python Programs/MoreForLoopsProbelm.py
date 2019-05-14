"""
1.Iterating through a string using range() and a for loop
a.create a string and assign it to a variable
b.use a for loop without a range() to iterate through and print the contents of the string from step 1.a.
c.use a for loop with a range() to iterate through and print the contents of the string from step 1.a.

2.Using , and end to print output of a for loop on the same line
a.create a variable and assign it a list of integers
b.use a for loop with , and end to print all the integers from the list you made as one integer (eg if your list was
 [1, 2, 5, 7], the output of the for loop should be 1257)
c.use a for loop with , and end to print all the integers from the list you made with "X" between them (eg if your list
 was [4, 3, 2, 1], the output of the for loop should be 4X3X2X1X)

3.Using a for loop to iterate through a dictionary
a.create a dictionary and assign it to a variable
b.use a for loop to iterate through the dictionary and print its keys and values with the following form:
 value key (eg, if your dictionary is {"first": 1, "second": 2}, your output should be 1 "first" and on another line
 2 "second")(since dictionaries don't have to print in order, your output with {"first": 1, "second": 2} as your
 dictionary could have also been 2 "second" and on another line 1 "first")

4.zip()
a.create 2 lists of numbers and assign them to variables
b.use a for loop and zip() to iterate through both those lists, sum their values, and append those values to a new list
 (eg, if one of your lists is [1, 2] and your other list is [5, 9], then the for loop would iterate through them,
 add 1 to 5 resulting in 6 and add 2 to 9 resulting in 11)
c.print the new list (the resulting list from the example given in 4.b. would be [6, 11])

5.for/else
a.create a tuple with 5 elements that are all strings and assign it to a variable
b.create a for/else loop that prints the first 4 elements of the tuple from step 5.a. with its for loop portion and
 the fifth element of the tuple from step 5.a. with the else statement
c.create a for/else loop that prints the first 3 elements of the tuple from step 5 then ends prematurely before the else
 statement is triggered using a break statement
"""
#1
str1 = "hello"
for char in str1:
 print(char)

#with range()

for char in range(len(str1)):
 print(str1[char])

#2
varList=[1,2,5,7]
for ele in varList:
 print(ele,end="")

varList = [4,3,2,1]
for ele in varList:
 print(ele, end="X")

#3
dict = {"first":1,"second":2}
for key in dict:
 print(str(dict[key])+" "+key)

#4
lista = [1,2]
listb = [5,9]
emptyl =[]

for item1, item2 in zip(lista,listb):
 emptyl.append(item1+item2)

print(emptyl) # u are a real genious gurl!!! u got this! keep grinding , keep pressing !!!!<3 love ya <3

#5
tups = ["one","two","three","four","five"]

for ele in range(len(tups)):
 if ele!=len(tups):
  print(tups[ele])
 else:
  print(tupes[len(tups)])# OMG!!! You are mind blowingly intelligent!!!! <3

for ele in range(len(tups)):
 if ele<(len(tups))-2:
  print(tups[ele])
 else:
  break
else:
  print("rest of the items")

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

string = "Tokyo"
integerlist = [1,2,3,4]
dictionary = {"one":1,"two":2}

for char in range(len(string)):
 print(string[char])

for ele in integerlist:
 print(ele,end="")

for key in dictionary:
 print(key + " " + str(dictionary[key]))

integerlist2 = [5,6,4,7]
for item1,item2 in zip(integerlist,integerlist2):
 if(item1>item2):
  print(item1)
 elif(item1<item2):
  print(item2)

for ele in integerlist:
 print(ele,end="")
else:
 print(9)