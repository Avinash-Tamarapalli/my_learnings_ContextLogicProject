w=eval(input("Enter the weight of the person(kg):"))
h=eval(input("Enter the height of the person(m):"))
BMI=round((w/(h*h)),1)
if (w<=0 or h<=0):
    print("Provide a valid input")
elif(BMI>=27.5):
    print("Your BMI is;",BMI,"(High Risk)")
elif(27.4>=BMI>=23):
    print("Your BMI is:",BMI,"(Moderate Risk)")
elif(22.9>=BMI>=18.5):
    print("Your BMI is:",BMI,"(Low Risk)")
elif(BMI<=18.5):
    print("Your BMI is:",BMI,"(Risk of nutritional deficiency diseases)")
