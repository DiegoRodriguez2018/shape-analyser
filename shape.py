import math 

def get_distance(p1,p2):
  dist = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
  return dist

# equation of a line y = mx + b
def get_slope(p0,p1):
  delta_x = p0[0]-p1[0]
  delta_y = p0[1]-p1[1]
  if delta_x!=0:
    return delta_y/delta_x
  else:
    return "infinite"

def get_b(p0,slope):
  # equation of a line, y = mx + b
  # so, b = y -mx, and using the first point
  # b = po[1] - slope*po[0]
  if slope !="infinite":
    return p0[1] - slope*p0[0]
  else:
    return "none"

def calculate_radius(point, h, k):
  # equation of a circle, (x - h)**2 + (y - k)**2 = r**2 
  x = point[0]
  y = point[1]
  radius = math.sqrt((x - h)**2 + (y - k)**2) 
  return radius

def is_triangle(edged, p0, p1):
  rows =  len(edged) # number of rows
  cols = len(edged[0]) # number of cols

  print(p0, p1)
  slope = get_slope(p0,p1)
  b = get_b(p0,slope)

  def get_distribution(slope, b, p0):
    left_dist = 0
    right_dist = 0
    for row in range(0,rows):
      if slope != "infinite":
        x_intersection = (row - b)/slope
      else:
        x_intersection = p0[0]
      epsilon = 5
      for col in range(0,cols):
        value = edged[row, col]
        if value != 0:
          if col<x_intersection - epsilon :
            left_dist += 1
          elif col>x_intersection + epsilon:
            right_dist += 1
    total_points = left_dist + right_dist
    return [left_dist*100/total_points,right_dist*100/total_points]

  dist = get_distribution(slope, b, p0)
  print(dist, "%")
  tolerance = 2
  if (dist[0] < tolerance or dist[1] < tolerance):
    return True
  else:
    return False

def is_circle(edged):
  rows =  len(edged) # number of rows
  cols = len(edged[0]) # number of cols

  xmax=0
  xmin=rows
  ymax=0
  ymin=cols
  coordinates = []
  for row in range(0,rows):
    for col in range(0,cols):
      var = edged[row, col]
      if var != 0:
        coordinates.append([row,col])
        if row<xmin:
          xmin = row
        if row>xmax:
          xmax = row
        if col<ymin:
          ymin = col
        if col>ymax:
          ymax = col
  radius = (xmax - xmin)/2 
  center = [xmin + radius ,  ymin + radius]
  h = center[0]
  k = center[1]
  tolerance = 2
  for point in coordinates:
    difference = abs(calculate_radius(point, h, k)-radius) # absolute value of the difference
    if difference>tolerance:
      return False
  return True