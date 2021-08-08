student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

nrOfHeights = 0
heightstSum = 0
for height in student_heights:
  nrOfHeights += 1
  heightstSum += height
avrHeight = round(heightsSum/nrOfHeights)
print(f"Averege Height equals: {avrHeight}")
