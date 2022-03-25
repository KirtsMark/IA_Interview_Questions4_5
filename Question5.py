def printstars(numberofstars):
    for i in range(0,numberofstars):
        for j in range(i,numberofstars):
            print(" ",end="")
        print(i+1,end="")
        for k in range(0,2):
            for l in range(0,i):
                print("*",end="")
        print(i+1,end="")
        print("\n",end="")
    for i in range(numberofstars-1,0,-1):
        for j in range(i,numberofstars+1):
            print(" ",end="")
        print(i,end="")
        for k in range(0,2):
            for l in range(0,i-1):
                print("*",end="")
        print(i,end="")
        print("\n",end="")
printstars(9)
