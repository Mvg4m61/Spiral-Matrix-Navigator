def spiral():
    l=[]
    m = int(input("\nEnter number of rows: "))
    n = int(input("\nEnter number of columns: "))
    for i in range(m):
        a=[]
        for j in range(n):
            num = int(input("\nEnter element: "))
            a.append(num)
        l.append(a)
    #display matrix
    for i in range(m):
        
        for j in range(n):
            print(l[i][j],end=' ')
        print("\n")
    count = 0
    stop = m*n
    i=0
    j=0
    r=m-1
    c=n-1
    flag=0
    while(count<stop):
        if i==c and j==c:
            print(l[i][j], end = ' ')
            count+=1
        for x in range(i,c):
            print(l[i][x],end = ' ')
            count+=1
        for x in range(i,r):
            print(l[x][c],end = ' ')
            count+=1
        for x in range(c,i,-1):
            print(l[r][x],end = ' ')
            count+=1
        for x in range(r,i,-1):
            print(l[x][j],end = ' ')
            count+=1
        i=i+1
        j=j+1
        r=r-1
        c=c-1
spiral()