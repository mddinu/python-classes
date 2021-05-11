def findword( sentence,word):
    c = sentence.split(" ")
    for i in c:
        if (i == word):
            return True
    return False
   
c = " good bye"
word ="good"
if (findword( c,word)):
    print("yes")
else:
    print("no")                  
