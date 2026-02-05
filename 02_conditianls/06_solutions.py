distance = int(input("Provoide distance :"))
 
if distance < 3:
    transportation = "walk"
elif distance <15:
    transportation="bike"
else:
    transportation="car"      
 
print(transportation)   