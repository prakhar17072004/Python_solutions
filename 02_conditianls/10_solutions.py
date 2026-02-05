pet_type= input("Provide the type :").lower()
pet_age = int(input("Provide the age :"))

if pet_type =="dog":
    if pet_age <2:
         food = "Puppy food"
    else:
         food="Adult food"
elif pet_type =="cat":
     if pet_age>5:
          food="Senior oat food"
     else:
          food="junior oat food" 

print(pet_type,"recommanded food is :",food)          

  
     
        
    
    

