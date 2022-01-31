# Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args):
    fun_name = function.__name__
    output = function(args[0], args[1], args[2])
    return f"You called {fun_name}{args}\nIt returned: {output}"
  return wrapper

# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return(a + b + c)

func = a_function(1, 2, 3)
print(func)
