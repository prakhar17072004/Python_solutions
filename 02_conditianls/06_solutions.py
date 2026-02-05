distance = int(input("Provoide distance :"))
 
if distance < 3:
    transportation = "walk"
elif distance <=15:
    transportation="bike"
else:
    transportation="car"      
 
print("The best transprot medium according to distance is ",transportation)   