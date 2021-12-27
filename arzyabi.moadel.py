a = input("name: ")
b = input("family: ")
c = float(input("nomre dars aval"))
d = float(input("nomre dars dovom"))
e = float(input("nomre dars sevom"))
moadel = ((c + d + e )/3 )
if moadel >= 17:
     print("status:""great")
if moadel >=12 and moadel< 17 :
    print("status:""normal")
if moadel <12 :
    print("status:""fail")
print(a ,b , moadel)
