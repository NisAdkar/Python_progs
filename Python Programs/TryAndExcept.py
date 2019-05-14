
"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
 second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
 second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""
"""
var1 = input("enter a variable")
var2 = input("enter another variable")

def fun(a,b):
 try:
  try:
   print(int(a)/int(b))
  except ZeroDivisionError:
   print("cannot devide by zero")
 except:
  print("both the variable needs to be integers")

fun(var1,var2)
"""
"""
def fun(a,b):
 try:
  print(int(a)/int(b))
 except ZeroDivisionError:
  print("cannot devide by zero")
"""
from random import randint
vara= input("enter an integer")
varb=randint(0,5)
print(varb)
try:
 if(varb>int(vara)):
  print(varb)
 elif(varb<int(vara)):
  print(vara)
 else:
  print("both are equal")
except:
  print("you need to enter the integer. pls run the prog again")
#you are the best Nis !!!! you are stronger and bigger than any of the programs in fromt of you !!
#Just hold the line and forge forward !!! you got this!!! you  are powerful!! you are the universer!! <3 love you & thank you for
# staying till the end !! for fighting till the end !! for pressing on!!! see where it got you !! you completed python tutorials in
# 3 days yo!!  Preeing on and holding the line and handeling the situation by centering yourself with the universe has tremondous power
# in it!!!!<3!! Keep going!!!! with the diamond heart!! YOU ARE NEVER ALONE ! UNIVERSER IS IN YOU!!<3<3<3<3