marks = int(input("Provide the marks :"))

if marks >100:
    print("Provide valid input")
    exit()
if marks >=90:
    print("A grade")   
elif marks >=80:
    print("B grade")
elif marks >= 70:
    print("C grade")  
elif marks >=60:
    print("D grade")
else:
    print("F grade")
