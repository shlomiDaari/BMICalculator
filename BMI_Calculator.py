#BMI Calculator
units = int((input("For calculate in kg and m type 1, for calculate in ibs and in type 2:  ")))#Enter your units that you familier with
normal_weight = "The normal weight BMI is between 18.5 to 25"
if units == 1:
    weight = float(input("What is your weight?(kg) "))#enter weight
    hight = float(input("What is your hight?(m) ")) #enter hight
    BMI = round(weight/hight ** 2) #BMI formola for kg and m
    the_ideal_weight_b = round(18.5*hight ** 2)#ideal bottom weight    for your hight
    the_ideal_weight_t = round(25*hight ** 2) #ideal top weight for your hight

    if BMI < 18.5:
        print(f"You are underweight, your BMI result is {BMI} {normal_weight} ")
         
    elif BMI < 25:
        print(f"You are in normal weight, your BMI result is {BMI} {normal_weight}")
        
    elif BMI < 30:
        print(f"you are overweight, your BMI result is {BMI} {normal_weight}")

    else:
        print(f"Obese!, your BMI result is {BMI} {normal_weight}")
    #print ideal weight for your given hight      
    print(f"Your ideal weight is between {the_ideal_weight_b} to {the_ideal_weight_t} better is between")        
else:
    weight = float(input("What is your weight?(ibs) "))#enter weight
    hight = float(input("What is your hight?(in) "))#enter hight
    BMI = float(703*weight/hight ** 2)#BMI formola for ibs and inch
    the_ideal_weight_b = round(703*18.5*hight ** 2) #ideal bottom weight    for your hight 
    the_ideal_weight_t = round(703*25*hight ** 2)#ideal top weight for your hight
   
    if BMI < 18.5:
        print(f"You are underweight, your BMI result is {BMI} {normal_weight} ")
        
    elif BMI < 25:
        print(f"You are in normal weight, your BMI result is {BMI} {normal_weight}")
        
    elif BMI < 30:
        print(f"you are overweight, your BMI result is {BMI} {normal_weight}")
         
    else:
        print(f"Obese!, your BMI result is {BMI} {normal_weight}")
    #print ideal weight for your given hight    
    print(f"Your ideal weight is between {the_ideal_weight_b} to {the_ideal_weight_t} better is between") 

