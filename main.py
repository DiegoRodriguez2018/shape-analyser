import cv2
import math
import shape

#reading file
# filename = 'circle.png'
filename = 'img/triangle.png'
# filename = 'quadrilateral.png'
# filename = 'quadrilateral2.png'
# filename = 'trapezoid.png'
img = cv2.imread(filename)
# Finding edges with Canny algorithm
edged = cv2.Canny(img, 30, 200)

rows =  len(edged) # number of rows
cols = len(edged[0]) # number of cols

#instead of top right needs to be the top left corner
def get_top_right():
  for y in range(0,rows):
    for x in range(0,cols):
      value = edged[y][x]
      if value != 0:
        return [x,y]

def get_bottom_left():
  for row in range(0,rows):
    for col in range(0,cols): 
      y = rows - 1 - row
      x = cols - 1- col
      value = edged[y][x]
      if value != 0:
        return [x,y]

p0 = get_top_right()
p1 = get_bottom_left()

def analyze(edged, p0, p1):
  if shape.is_triangle(edged, p0, p1):
    return("It's a triangle")
  elif shape.is_circle(edged):
    return("It's a circle")
  else:
    return("It's a quadrilateral")

caption = analyze(edged, p0, p1)

result = edged


# displaying result
cv2.imshow(caption, result)
cv2.waitKey()
