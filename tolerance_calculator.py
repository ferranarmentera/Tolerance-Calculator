# tolerance calculator considers the material and level of precicion of the parts
# variables definition quality leve
coarsev = 0.0075
mediumv = 0.005
highv = 0.003
POR = 0.003
uservalue = float(input("enter the dimension value  "))
numberofcavities = float(input("enter the number of cavities  "))
if numberofcavities == 1:
    cavityFactor = 1
elif numberofcavities == 2:
    cavityFactor = 1.05
elif numberofcavities == 4 or 6:
    cavityFactor = 1.1
elif numberofcavities == 8:
    cavityFactor = 1.13
elif numberofcavities == 8:
    cavityFactor = 1.15
elif numberofcavities == 16:
    cavityFactor = 1.2
else:
    print("wrong cavity number")


uservalue_quality = input("Enter the quality level : coarse ,medium , high ")
if uservalue_quality == "coarse":
    x = uservalue*coarsev*cavityFactor
    print("toleance range is:", x)
elif uservalue_quality == 'medium':
    x = uservalue*mediumv*cavityFactor
    print("toleance range is:", x)
elif uservalue_quality == 'high':
    x = uservalue*highv*cavityFactor
    print("toleance range is:", x)
else:
    print("not entered value")
