import math
def areaCircum(rad):
    area =math.pi*rad*rad
    circum =2*math.pi*rad
    return area ,circum

a,c = areaCircum(4)
print("area :",a,"circumference:",round(c,2))
