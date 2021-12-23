import math
a = float(input("adad aval"))
b = float(input("adad dovom"))
print("amaliat ha:","*,+,-,/,sin,cos,rishe,tavan 2")
op = input("amaliat riazi mored nazar:")
if op=="+":
    javab = a + b
if op=="-":
    javab = a - b
if op=="*":
    javab = a * b
if op=="/":
    if b==0:
        javab = "can't divide by zero"
    else:
        javab = a / b
if op=="sin":
    javab = ( "sinus adad aval :",(math.sin(math.radians(a))),"sinus addad dovom:",  (math.sin(math.radians(b))))
if op=="cos":
    javab = ( "cosinus addad aval :", (math.cos(math.radians(a))), "cosinus addad dovom:", (math.cos(math.radians(b))))
if op=="rishe":
    javab = ("aval:",(math.sqrt(a)),"dovom:",(math.sqrt(b)))
if op=="tavan 2":
    javab = ("aval:", (a*a), "dovom:", (b*b))
print(javab)
