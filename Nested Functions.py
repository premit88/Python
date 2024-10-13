# Key to understading all this is compile time of python. 
# There is a misconception that Python is not compiled, infact it is compiled and
# also interpreted. Source code is first compiled to byte code, then the 
# interpreter, interprets the bytecode at runtime. Compilation happens first. 

# Remember Rule : Variable lookup happens at the runtime, but where python will look
# for the variable is determined at the compile time. 


# Level 1 : 
# We just say return x, and there is no 'x' argument passed. The only 'x' used
# w.r.t function is the global x. The code for every function is compiled at 
# compile time. There are no assignemnt to 'x' in this or any other enclosing 
# function scope. Hence the compiler decides to look in the global namespace for 'x'. 

x = "Global value of x"

def lev_1():
  return x

print(lev_1())


# Level 2 :
# We are again returning 'x', but in this case we take an argument 'v', if 'v' is TRUE, 
# we will assign a local variable (dynamically typed). So which 'x' will be returned ?
# Remember : Where we look for 'x' needs to be determined at compile time. 
def lev_2(v):
  print(v)
  if v == True:
    x = "Local value of x"
    return x

print(lev_2(True))










# x = "global x"
# 
# def level_six():
#   z = "Outer Z"
# 
#   def donky():
#     def inner(y):
#       return x, y, z
# 
#     z = "donky z"
#     return inner
# 
#   def chonky():
#     x = "Chonky x"
#     f = donky()
#     return f("y arg")
# 
#   return chonky()
# 
#   #
#   level_six()
# 
