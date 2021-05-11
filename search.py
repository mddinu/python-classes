import re 
a = "good bye"
b = re.search("^good", a)
if b:
    print("yes")
else:
    print("no")
        

                    
