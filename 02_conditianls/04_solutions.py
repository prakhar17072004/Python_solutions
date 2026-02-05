fruit = "Banana"
color = input("Provide the color of banana: ").lower()

if fruit == "Banana":
    if color =="green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")   
    elif color == "brown":
        print("OverRipe") 
    else:
        print("Provide the valid color")         