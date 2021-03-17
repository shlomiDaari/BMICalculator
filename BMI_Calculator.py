#BMI Calculator
units = int((input("For calculate in kg and m type 1, for calculate in ibs and in type 2:  ")))
normal_weight = "The normal weight BMI is between 18.5 to 25"
if units == 1:
    weight = float(input("What is your weight?(kg) "))
    hight = float(input("What is your hight?(m) "))
    BMI = round(weight/hight ** 2)
    the_ideal_weight_b = round(18.5*hight ** 2)       
    the_ideal_weight_t = round(25*hight ** 2)
    
    if BMI < 18.5:
        print(f"You are underweight, your BMI result is {BMI} {normal_weight} ")
         
    elif BMI < 25:
        print(f"You are in normal weight, your BMI result is {BMI} {normal_weight}")
        
    elif BMI < 30:
        print(f"you are overweight, your BMI result is {BMI} {normal_weight}")

    else:
        print(f"Obese!, your BMI result is {BMI} {normal_weight}")
    print(f"Your ideal weight is between {the_ideal_weight_b} to {the_ideal_weight_t} better is between")        
else:
    weight = float(input("What is your weight?(ibs) "))
    hight = float(input("What is your hight?(in) "))
    BMI = float(703*weight/hight ** 2)
    the_ideal_weight_b = round(703*18.5*hight ** 2)      
    the_ideal_weight_t = round(703*25*hight ** 2)
   
    if BMI < 18.5:
        print(f"You are underweight, your BMI result is {BMI} {normal_weight} ")
        
    elif BMI < 25:
        print(f"You are in normal weight, your BMI result is {BMI} {normal_weight}")
        
    elif BMI < 30:
        print(f"you are overweight, your BMI result is {BMI} {normal_weight}")
         
    else:
        print(f"Obese!, your BMI result is {BMI} {normal_weight}")
    print(f"Your ideal weight is between {the_ideal_weight_b} to {the_ideal_weight_t} better is between") 

