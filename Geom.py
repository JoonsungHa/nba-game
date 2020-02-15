import math

#  File: Geom.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance to other which is another Point object
    def dist(self, other):
        return abs(math.sqrt((other.x - self.x) * (other.x - self.x) + (other.y - self.y) + (other.y - self.y)))

    # create a string representation of a Point (x, y)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # test for equality between two points
    def __eq__(self, other):
        if abs(self.y - other.y) < 1.0e-6 and abs(self.x - other.x) < 1.0e-6:
            return True
        return False


class Line(object):
    # line is defined by two Point objects p1 and p2
    # constructor assign default values if user does not define
    # the coordinates of p1 and p2 or the two points are the same
    def __init__(self, p1_x=0, p1_y=0, p2_x=1, p2_y=1):
        self.p1 = Point(p1_x, p1_y)
        self.p2 = Point(p2_x, p2_y)

    # returns True if the line is parallel to the x axis
    # and False otherwise
    def is_parallel_x(self):
        if abs(self.slope() - 0) < 1.0e-6:
            return True
        return False

    # returns True if the line is parallel to the y axis
    # and False otherwise
    def is_parallel_y(self):
        if self.slope() == math.inf:
            return True
        return False

    # determine slope for the line
    # return float ('inf') if line is parallel to the y-axis
    def slope(self):
        if abs(self.p2.x - self.p1.x) < 1.0e-6:
            if abs(self.p2.y - self.p1.y) > 1.0e-6:
                return math.inf
        if self.p2.x > self.p1.x:
            return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)
        if self.p2.x < self.p1.x:
            return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
        return 'Error'

    # determine the y-intercept of the line
    # return None if line is parallel to the y axis
    def y_intercept(self):
        if self.is_parallel_y():
            return None
        return Point(0, self.p1.y - self.slope() * self.p1.x)

    # determine the x-intercept of the line
    # return None if line is parallel to the x axis
    def x_intercept(self):
        if self.is_parallel_x():
            return None
        else:
            return Point(self.p1.x - self.slope() * self.p1.y,0)
        

    # returns True if line is parallel to other and False otherwise
    def is_parallel(self, other):
        if abs(self.slope() - other.slope()) < 1.0e-6:
            return True
        return False

    # returns True if line is perpendicular to other and False otherwise
    def is_perpendicular(self, other):
        if abs(self.slope() - (1 / other.slope()) * -1) < 1.0e-6:
            return True
        return False

    # returns True if Point p is on the line or an extension of it
    # and False otherwise
    def is_on_line(self, p):
        if abs(p.x * self.slope() + self.y_intercept() - p.y) < 1.0e-6:
            return True
        return False

    # determine the perpendicular distance of Point p to the line
    # return 0 if p is on the line
    def perp_dist(self, p):
        line= Line(p.x, p.y, (p.x + (self.p1.x - self.p2.y)), (p.y - (self.p1.y - self.p2.y)))
        return p.dist(self.intersection_point(line))

    
    # returns a Point object which is the intersection point of line
    # and other or None if they are parallel
    def intersection_point(self, other):
        
        x_coor = ((other.p1.y - (other.slope() * other.p1.x)) - (self.p1.y - (self.slope() * self.p1.x))/ (self.slope() - other.slope()))
        y_coor = self.slope() * x_coor - (self.p1.y - (self.slope() * self.p1.x))

        return Point(x_coor,y_coor)

    # return True if two points are on the same side of the line
    # and neither points are on the line
    # return False if one or both points are on the line or both
    # are on the same side of the line
    def on_same_side(self, p1, p2):
        print("SDFDS",type(p1))
        print("dsfSAEW",type(self.y_intercept()))
        if p1.y < (self.slope() * p1.x + self.y_intercept()) and p2.y < (self.slope() * p2.x + self.y_intercept()):
            return True
        elif p1.y > (self.slope() * p1.x + self.y_intercept()) and p2.y > (self.slope() * p2.x + self.y_intercept()):
            return True
        return False
        

    # string representation of the line - one of three cases
    # y = c if parallel to the x axis
    # x = c if parallel to the y axis
    # y = m * x + b
    def __str__(self):
        if self.is_parallel_x():
            return "y = " + str(self.y_intercept().y)
        if self.is_parallel_y():
            return "x = " + str(self.x_intercept().x)
        return "y = " + str(self.slope()) + "x + " + str(self.y_intercept().y)


def is_equal (a, b):
  tol = 1.0e-6
  return (abs (x - y) < tol)



def main():
  # open file "geom.txt" for reading
    data = open("geom.txt","r")
    

  # read the coordinates of the first Point P
    p_coor = data.readline()
    p_coor = p_coor.split()
    
    

  # read the coordinates of the second Point Q
    q_coor = data.readline()
    q_coor = q_coor.split()

    
    q_value = Point(float(q_coor[0]),float(q_coor[1]))
    p_value = Point(float(p_coor[0]),float(p_coor[1]))


  # print the coordinates of points P and Q
    print("Coordinates of P: ",end = "")
    print(p_value)
    print("Coordinates of Q: ",end="")
    print(q_value)

  # print distance between P and Q
    print("Distance between P and Q:",p_value.dist(q_value))
    

  # print the slope of the line PQ
    p_line = Line(float(p_coor[0]),float(p_coor[1]),float(q_coor[0]),float(q_coor[1]))
    print("Slope of PQ:", p_line.slope())
  

  # print the y-intercept of the line PQ
    print("Y-Intercept of PQ:",p_line.y_intercept())

  # print the x-intercept of the line PQ
    print("X-Intercept of PQ:",p_line.x_intercept())

  # read the coordinates of the third Point A
    a_coor = data.readline()
    a_coor = a_coor.split()
    
			 
  # read the coordinates of the fourth Point B
    b_coor = data.readline()
    b_coor = b_coor.split()
    

    a_value = Point(float(a_coor[0]),float(a_coor[1]))
    b_value = Point(float(b_coor[0]),float(b_coor[1]))



  # print the string representation of the line AB
    a_line = Line(float(a_coor[0]),float(a_coor[1]),float(b_coor[0]),float(b_coor[1]))
    print("Line AB:",a_line)


  # print if the lines PQ and AB are parallel or not
    if a_line.is_parallel(p_line):
        print("PQ is parallel to AB")
    else:
        print("PQ is not parallel to AB")

  # print if the lines PQ and AB (or extensions) are perpendicular or not
    if a_line.is_perpendicular(p_line):
        print("PQ is perpendicular to AB")
    else:
        print("PQ is not perpendicular to AB")

  # print coordinates of the intersection point of PQ and AB if not parallel
    if a_line.is_parallel(p_line) == False:
        print("Intersection point of PQ and AB:",a_line.intersection_point(p_line))

  # read the coordinates of the fifth Point G
    g_coor = data.readline()
    g_coor = g_coor.split()

  # read the coordinates of the sixth Point H
    h_coor = data.readline()
    h_coor = h_coor.split()

  # print if the the points G and H are on the same side of PQ

    g_line = Line(float(g_coor[0]),float(g_coor[1]),float(h_coor[0]),float(h_coor[1]))
    
    if g_line.on_same_side(p_value,q_value) == True:
        print("G and H are on the same side of PQ")
    else:
        print("G and H are not on the same side of PQ")
    

  # print if the the points G and H are on the same side of AB
    if g_line.on_same_side(g_value,h_value) == True:
        print("G and H are on the same side of PQ")
    else:
        print("G and H are not on the same side of PQ")

  # close file "geom.txt"
    data.close()
    

if __name__ == "__main__":
  main()
