

'''
edges = cv2.Canny(img,100,200)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    print(cv2.arcLength(contour,closed=0))
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('Image',img)
'''


'''
def check_intersection(r1,r2):
    if ((r1[2]  <  r2[0])  or  (r1[0]   >  r2[2])  or (r1[1] >  r2[3]) or (r1[3]<r2[1]) ):
        return False
    else:
        return True
'''
image=img.copy()
result = image.copy()
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,1))
remove_horizontal = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(blank, [c], -1, (255,0,255), 5)

# Remove vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,40))
remove_vertical = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    cv2.drawContours(blank, [c], -1, (255,0,255), 5)
kernel = np.ones((2,2),np.uint8)
'''
