#Question 9

angle = int(input('Enter an angle(-180,180):'))
if angle < 180 and angle > -180:
    angleE = 360 - abs(angle)
    print('Equivalent angle:', angleE)
else:
    angleE = 360 - abs(angle)
    print('Error')
