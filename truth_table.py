ni=int(input('No. of inputs : '))
ng=int(input("No. of gates : "))
nt=ng-1
i = [0,0,0,0,0,0,0,0]
g = []
for j in range(0,ng) :
    print("Gate "+str(j+1))
    g.append([int(input("Gate : ")),int(input("Input 1 : ")),int(input("Input 2 : "))])

'''
11 => AND
12 => OR
13 => NOT
14 => NAND
15 => NOR
16 => XOR
17 => XNOR
'''


def output(G):
    if(G[0]==13):
        return (i[G[1]-1]*(-1)+1)
    elif(G[0]==11):
        return (i[G[1]-1]&i[G[2]-1])
    elif(G[0]==12):
        return (i[G[1]-1]|i[G[2]-1])
    elif(G[0]==14):
        return ((i[G[1]-1]&i[G[2]-1])*(-1)+1)
    elif(G[0]==15):
        return ((i[G[1]-1]|i[G[2]-1])*(-1)+1)
    elif(G[0]==16):
        return (i[G[1]-1]^i[G[2]-1])
    elif(G[0]==17):
        return ((i[G[1]-1]^i[G[2]-1])*(-1)+1)


if(ni==1):
    print("Red Output")
    for j in (0,1):
        i[0]=j
        for x in (0,nt-1):
            i[x+3]=output(g[x])

        o=output(g[ng-1])
        print(str(j)+"     "+str(o))


elif(ni==2):
    print("Red Green Output")
    for j in (0,1):
        for k in (0,1):
            i[0]=j
            i[1]=k
            for x in (0,nt-1):
                i[x+3]=output(g[x])

            o=output(g[ng-1])
            print(str(j)+"   "+str(k)+"     "+str(o))


elif(ni==3):
    print("Red Green Blue Output")
    for j in (0,1):
        for k in (0,1):
            for l in (0,1):
                i[0]=j
                i[1]=k
                i[2]=l
                for x in (0,nt-1):
                    i[x+3]=output(g[x])

                o=output(g[ng-1])
                print(str(j)+"   "+str(k)+"     "+str(l)+"    "+str(o))
