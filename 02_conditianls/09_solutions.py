year =int(input("Provide year :"))

if year % 400 == 0:
    print(year," Leap year")
elif (year %4== 0 and year % 100 !=0):
    print(year," leap year")
else:
    print(year," not leap year")
