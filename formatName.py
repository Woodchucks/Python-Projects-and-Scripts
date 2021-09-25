def format_name():
  f_name = input("What's your first name? ").title()
  l_name = input("What's your last name? ").title()
  return f_name + " " + l_name

output = format_name()
print(output)
