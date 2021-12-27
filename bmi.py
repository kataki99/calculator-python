a = float(input("ghad bar hasb meter"))
b = float(input("vazn bar hasb Kg"))
bmi = b / (a*a)
print(bmi)
if bmi <18.5:
    print("bmi underweight")
if bmi >= 18.5 and bmi<= 24.9:
    print("bmi normal")
if bmi>=25 and bmi<=29.9:
    print("bmi overweight")
if bmi>=30 and bmi <=34.9:
    print("bmi obese")
if bmi>=35:
    print("extremly obese")
