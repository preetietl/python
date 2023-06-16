#age=50
age=int(input("enter your age"))

if age> 18:
 print("you are elligible to vote")
else: 
 print("you r not elligible to vote")


dictionary={"one":1, 
            "two":2,
            "three":3}

age=input("enter your age")
age1=dictionary.get(age)    # get function will return None if any value is not assigned in dictionary.
print(age1)

if  not age1 :
 print("wrong input")
elif age1>2:
 print("you are elligible to vote")
else: 
 print("you r not elligible to vote")


 
