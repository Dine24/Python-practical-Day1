n=int(input("enter the num of fresh loves purchaced:"))
o=int(input("enter the num of day old loves purchaced:"))
r=int(input("regular price of lovas:"))
print("regular price:",r)
print("amount of new lovas",n*r)
print("amount of day old lovas",(r-(60/100)*185)*o)
print("total smount",(n*r)+(r-(60/100)*185)*o)

 



