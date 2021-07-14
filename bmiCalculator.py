height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_as_float = float(height)
weight_as_float = float(weight)

bmi = weight_as_float/(height_as_float**2)

print(int(bmi))
