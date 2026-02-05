#prime number
n = int(input("Provide the value :"))

is_prime=True

if n >1:
    for i in range(2,n):
        if(n%i)==0:
            is_prime=False
            break

    if is_prime:
        print("Number is prime")
    else:
        print("Not prime") 
else:
    print(" Numberis not prime") 

       
