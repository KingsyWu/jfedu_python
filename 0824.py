def q(a):
    for i in a:
        for j in a:
            if i < j :
                #print("A"+str(i) + "\t" + str(j) + "\n")
                #a[i],a[j] = a[j],a[i]
                i, j = j, i
                #print(str(i)+"\t"+str(j)+ "\n")
                #print(a[3])
        #print(str(i) + "\t" + str(j) + "\n")
                #print(a)
    print(a)
a = [1,3,2,5,4]
q(a)