import os
counter = 1
for i in range(50):
    a =os.mknod(counter * str(i) + '.py')
    print(a)	
