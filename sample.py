import os
a = os.getcwd()
b = input("enter the filename:")
c =os.path.join(a,b)
if os.path.isfile(c):
   print("yes")
else:
   print("no")
   os.mknod(c)
   
with open(c, "r") as f:
    print(f.read())
      

