# Calculator

# ADD
def add(a, b):
  """Add two values"""
  return a + b

# SUBSTRACT
def substract(a, b):
  """Substract two values"""
  return a - b

# MULTIPLY
def multiply(a, b):
  """Multiply two values"""
  return a * b

# DIVIDE
def divide(a, b):
  """Divide two values"""
  if b == 0:
    return "Cannot divide through 0"
  return a / b

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide 
}

a = float(input("What's the first number for the caculation?"))

for operation in operations:
  print(operation)

pick_operation = input("Pick one symbol from the above: ")

b = float(input("What's the second number for the caculation? "))

calculation = operations[pick_operation]
res = calculation(a, b)

print(f"{a} {pick_operation} {b} = {res}")

next_calc = input("Do you want to make another calculation? Type 'y' for yes, 'n' for no. ")
while next_calc == 'y':
  for operation in operations:
    print(operation)
  pick_operation_2 = input("Pick one symbol from the above: ")
  c = float(input("What's the next number for the caculation? "))

  calculation = operations[pick_operation_2]
  res_2 = calculation(res, c)
  print(f"{res} {pick_operation_2} {c} = {res_2}")
  res = res_2
  next_calc = input("Do you want to make another calculation? Type 'y' for yes, 'n' for no. ")
