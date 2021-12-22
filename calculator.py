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
    javab = ( "sinus adad aval dar radian:",(math.sin(a)),"sinus addad dovom az radian:",  (math.sin(b)))
if op=="cos":
    javab = ( "cosinus addad aval az radian:", (math.cos(a)), "cosinus addad dovom az radain:", (math.cos(b)))
if op=="rishe":
    javab = ("aval:",(math.sqrt(a)),"dovom:",(math.sqrt(b)))
if op=="tavan 2":
    javab = ("aval:",(a**2),"dovom:"(b**2))
print(javab)
