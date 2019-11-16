import numpy as np
import cv2
import imutils
def length(l):
    p1x,p1y,p2x,p2y=l[0]
    return ((p1x-p2x)**2+(p1y-p2y)**2)**0.5
def unique(p1,p2):
    if length([[p1[0],p1[1],p2[0],p2[1]]])<10:
        return False
    else:
        return True
def ingate(gate,pt):
    mid=[[(gate[0][0]+gate[1][0])/2,(gate[0][1]+gate[1][1])/2,pt[0],pt[1]]]
    if length(mid)<50:
        return True
    else:
        return False
gate=""
'''
def parallel_lines(l1,l2):
    if min(distance(l1[0],l))

'''
img=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/T8.jpg')
xor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/xor.png')
xnor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/xnor.png')
andi=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/and.png')
nand=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/nand.png')
nor=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/nor.png')
or_=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/or.png')
not_=cv2.imread('/home/adit/Documents/Programming/projects/circuitx/gates/not.png')
gates_img=img.copy()
ni=0
red=  [np.array([0,50,50] ),np.array([10,255,255])]
green=[np.array([ 46,235,14]),np.array([ 66,255,264])]
blue=[np.array([100,234,173]),np.array([120,254,253])]
yellow=[np.array([ 18,245,213]),np.array([ 38,265,293])]
colors= [red,green,blue,yellow]
cnames=["red","green","blue","yellow"]
img_color = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# code to detect no of colors
kernel = np.ones((2,2), np.uint8)
colors_=[]
for i in range(3):
    number=0
    lower,upper = colors[i]

    img_color=cv2.dilate(img_color, kernel, iterations=1)
    mask=cv2.inRange(img_color,lower,upper)

    cnts,_ =  cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c=[]
    for cnt in cnts:

        if 144>cv2.contourArea(cnt)>10:
            ni+=1
            number+=1
            c.append(cnt[0])
    colors_.append([cnames[i],number,c])
for i in range(len(colors_)-1):
    print("No of "+colors_[i][0]+" inputs :"+str(colors_[i][1]))

templates = [xor,xnor,andi,nand,nor,or_,not_]
names=['xor','xnor','and','nand','nor','or','not']
copy=img.copy()
#img = cv2.dilate(img,kernel,iterations = 2)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold=[0.9,0.9,0.9,0.95,0.95,0.95,0.9]
gates=[[],[],[],[],[],[],[]]
ng=0
for i in range(len(templates)):
    template=cv2.cvtColor(templates[i], cv2.COLOR_BGR2GRAY)
    (tH, tW) = template.shape[:2]
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( result >= threshold[i])
    pts=[]
    for pt in zip(*loc[::-1]):
        pts.append([pt,(pt[0] + tW, pt[1] + tH)])
        cv2.rectangle(gates_img, pt, (pt[0] + tW, pt[1] + tH), (255,0,255), 1)
        cv2.putText(gates_img, names[i], pt, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
        ng+=1

        gate=names[i]
    gates[i]=[names[i],pts]

cv2.imshow("Gates",gates_img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
gray_copy=gray.copy()
#gray = cv2.erode(gray,kernel,iterations = 2)
height, width = img.shape[:2]
blank = 255 * np.ones(shape=[height,width,  3], dtype=np.uint8)



edged = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(gray,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(blank, contours, -1, (0, 255, 0), 3)
height, width = img.shape[:2]
blank = 255 * np.ones(shape=[height,width,  3], dtype=np.uint8)

unique_points=[]

lsd = cv2.createLineSegmentDetector(0)
lines,width,prec,_ = lsd.detect(gray)
drawn=[]
for i in range(len(lines)):
    if length(lines[i])>20:
        drawn_img = lsd.drawSegments(blank,lines[i])
        drawn.append(lines[i])

        flag1=True
        flag2=True

        if len(unique_points)==0:
            unique_points.append([lines[i][0][0],lines[i][0][1]])
            unique_points.append([lines[i][0][2],lines[i][0][3]])
            continue

        if len(unique_points)!=0:
            for j in range(len(unique_points)):
                if unique(unique_points[j],[lines[i][0][0],lines[i][0][1]])==False and unique(unique_points[j],[lines[i][0][2],lines[i][0][3]]):
                    flag1=False
                    flag2=False
                    break
                elif(unique(unique_points[j],[lines[i][0][0],lines[i][0][1]])==False):
                    flag1=False
                    break
                elif (unique(unique_points[j],[lines[i][0][2],lines[i][0][3]])==True):
                    flag2=False
                    break
                else:
                    continue
        if flag1==True  and len(unique_points)!=0:
            unique_points.append([lines[i][0][0],lines[i][0][1]])
            continue
        if flag2==True and len(unique_points)!=0:
            unique_points.append([lines[i][0][2],lines[i][0][3]])
#cv2.imshow("LD",drawn_img)
'''
for a in range(len(gates)):
    unique_gates=[]
    indexes=[]
    for i in range(len(gates[a][1])):
        for j in range(i+1,len(gates[a][1])):
            if unique(gates[a][1][i],gates[a][1][j])==False:
                indexes.append(j)
    for i in range(len(gates[a][1])):
        if i not in indexes:
            unique_gates.append([names[a],gates[a][1][i]])
    gates[a]=unique_gates'''
indexes=[]

u=[]
for i in range(len(unique_points)):
    for j in range(i+1,len(unique_points)):
        if unique(unique_points[i],unique_points[j])==False:
            indexes.append(j)
            indexes.append(i)

indexes.sort()
#u.append(unique_points[0])
u+=unique_points[0:indexes[0]]
for i in range(len(indexes)-1):
    u+=unique_points[indexes[i]+1:indexes[i+1]]
u+=unique_points[indexes[len(indexes)-1]:len(unique_points)]
unique_points=u

gatepts=[]
for pt in unique_points:
    for i in range(len(gates)):
        for j in range(len(gates[i][1])):
            if ingate(gates[i][1][j],pt):
                gatepts.append([names[i],pt])


for i in range(len(unique_points)):
    gates_img=cv2.circle(gates_img,(unique_points[i][0],unique_points[i][1]), 10, (255,0,0),1)

h=[]
for cnt in contours:
    if len(cnt)<1000:

        for i in range(len(gatepts)):
            for j in range(i+1,len(gatepts)):
                in1=[[int(gatepts[i][1][0]),int(gatepts[i][1][1])]]
                in2=[[int(gatepts[j][1][0]),int(gatepts[j][1][1])]]

                if (in1 in cnt) and (in2 in cnt) :
                    #print(cnt)
                    h.append((gatepts[i],gatepts[j]))

#drawn_img = lsd.drawSegments(blank,drawn)
#cv2.imshow("LSD",gates_img )
#ni=int(input('No. of inputs : '))
#ng=int(input("No. of gates : "))
'''nt=ng-1
i = [0,0,0,0,0,0,0,0]
for j in range(0,ng) :

    print("Gate "+str(j+1))
    g.append([int(input("Gate : ")),int(input("Input 1 : ")),int(input("Input 2 : "))])


11 => AND
12 => OR
13 => NOT
14 => NAND
15 => NOR
16 => XOR
17 => XNOR

if gate=="and":
    GATE=11
if gate=="or":
    GATE=12
if gate=="not":
    GATE=13
if gate=="nand":
    GATE=14
if gate=="nor":
    GATE=15
if gate=="xor":
    GATE=16
if gate=="xnor":
    GATE=17
if ni==1:
    g.append([GATE,1,1])
elif ni==2:
    g.append([GATE,1,2])

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
'''

cv2.waitKey(1000000)
cv2.destroyAllWindows()
