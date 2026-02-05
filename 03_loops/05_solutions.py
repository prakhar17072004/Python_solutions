# first non-repeating chracter

input_str = input("Provide the string :")

for char in  input_str:
    if input_str.count(char)==1:
        print("Char is :",char)
        break

