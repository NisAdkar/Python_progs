"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------



def fstring():
 print("Hello world")

a=5

def singVal(a):
 print(a)

fstring()
singVal(a)

"""
def none():
 print("something")
# 2.
five = 5
# 3.
def fiverr(a):
 print(a)
# 4.
none()
# 5.
fiverr(five)
"""


# ----------------------------------------------------------------------------------------------------------------------
"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

x=3
y=7
z=4

def diff(x,y):
 a=x-y;
 print(a)

def prod(x,y,z):
 b=x*y*z
 print(b)

diff(x,y)
prod(x,y,z)

# ----------------------------------------------------------------------------------------------------------------------
"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

i=3.0
j=5.0
k=6.0

def quoti(i,j):
 l=i/j
 return l

def requoti(r,s,t):
 return quoti(r,s)/t

result1 = quoti(i,j)

print(result1)
print(requoti(i,j,k))



# ----------------------------------------------------------------------------------------------------------------------

def val1(e):
 return e*2

def fun1(inta,intb):
 return inta*intb

def funinfun(u,v,w):
 print(fun1(val1(u),v)*w)

funinfun(7,4,2)



