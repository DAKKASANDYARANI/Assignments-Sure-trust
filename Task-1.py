#Take name
#Take height and weight as an input
#output BMI(body mass index) with customized output for different classes
#NOtE:account for all the mistakes the user might take

name=input("name:")
height=float(input("height"))
weight=float(input("weight:"))
BMI=weight/height*height
print(BMI)
if BMI>0:
    if BMI<18.5:
        print(f"{name} you are Underweight")
    elif BMI>=18.5 and BMI<25:
        print(f"{name} you are healthy")
    elif BMI>=25 and BMI<30:
        print(f"{name} you are Overweight")
else:
    print("f{name} Enter correct details")