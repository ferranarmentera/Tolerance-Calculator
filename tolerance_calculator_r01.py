# tolerance calculator considers the material and level of precicion of the parts
# variables definition quality leve


class Tolerance():
    def __init__(self, dimension, mat, cav, quality):
        self.dimension = dimension.values()
        self.mat = mat.values()
        self.cav = cav.values()
        self.quality = quality.values()

    def user_questions(self):
        print("-----")
        print("Linear Dimension" + " : " + self.dimension)
        print("Material" + " : " + self.mat)
        print("Number of Cavities" + " : " + self.cav)
        print("Quality Level " + " : " + self.quality)


def ask_user(message=''):
    user_input = ''
    while not user_input:
        user_input = input(message)
    return user_input


def form_complete(values, placement, length):
    placement = []
    while len(placement) < length:
        dimension = ask_user("Enter Dimension: ")
        mat = ask_user("Enter material: ")
        cav = ask_user("Enter number of cavities: ")
        quality = ask_user("Enter Quality level: ")
        values = Tolerance(dimension, mat, cav, quality)
        placement.append(values)
    return placement


if __name__ == '__main__':

    Tolerances = form_complete('Tolerance', 'Tolerances', 3)
    for a in range(len(Tolerance)):
        Tolerances[a].user_questions()

"""p1 = Person("John", 36)
p1.myfunc()
coarsev = 0.0075
mediumv = 0.005
highv = 0.003
POR = 0.003
uservalue = float(input("enter the dimension value  "))
numberofcavities = float(input("enter the number of cavities  "))
if numberofcavities == 1:
    cavityFactor = 1.0
elif numberofcavities == 2:
    cavityFactor = 1.03
elif numberofcavities == 4 or 6:
    cavityFactor = 1.08
elif numberofcavities == 8:
    cavityFactor = 1.15
elif numberofcavities == 16:
    cavityFactor = 1.2
elif numberofcavities == 32:
    cavityFactor = 1.25
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
    print("not entered value")"""
