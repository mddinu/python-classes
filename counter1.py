def count_occ(a,p):
    counter = 0
    for  data in range(1, a+1):
        if data%p == 0:
            counter += 1
    print(counter)
count_occ(100,5)       
            
