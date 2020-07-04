def read():
    arr=[]
    with open("input04.txt") as f:
        for line in f:
            arr.append([int(x) for x in line.split()])
    return arr

def write(outputINFO):
    with open("output.txt", "w") as file:
        for i in range(len(outputINFO)):
            print(outputINFO[i], file=file)

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Rectangle:
    def __init__(self,p1,p2):
        self.intersection=False
        self.p1=Point(p1.x,p1.y)
        self.p2=Point(p2.x,p2.y)
    
    @property
    def width(self):
        return abs(self.p1.x-self.p2.x)
        
    @property
    def height(self):
        return abs(self.p1.y-self.p2.y)

    def is_on_edge(p1,p2, tmpP1, tmpP2):
        # 1 point 
        p1.x
        if(p1.x==tmpP1.x)and(p1.y<tmpP1.y<p2.y): #левая грань
            return True

        if(p1.y==tmpP1.y)and(p1.x<tmpP1.x<p2.x): #нижняя грань
            return True
        # 2 point 
        if(p2.x==tmpP2.x)and(p1.y<tmpP2.y<p2.y):#правая грант
            return True

        if(p2.y== tmpP2.y)and(p1.x<tmpP2.x<p2.x):#верхняя грань
            return True
        # 3 point 
        if(p2.x==tmpP2.x)and(p1.y<tmpP1.y<p2.y):#правая грант
            return True

        if(p1.y==tmpP1.y)and(p1.x<tmpP2.x<p2.x): #нижняя грань
            return True
        # 4 point 
        if(p1.x==tmpP1.x)and(p1.y<tmpP2.y<p2.y): #левая грань
            return True

        if(p2.y== tmpP2.y)and(p1.x<tmpP1.x<p2.x):#верхняя грань
            return True

        return  False
    
    def is_inside(p1,p2, tmpP):
        if p1.x<tmpP.x<p2.x:
            if  p1.y<tmpP.y<p2.y:
                return True
        return False

    def is_intersect(self, other):
        if Rectangle.is_inside(self.p1,self.p2,other.p1) or Rectangle.is_inside(self.p1,self.p2,other.p2) or Rectangle.is_inside(self.p1,self.p2,Point(other.p1.x,other.p2.y)) or Rectangle.is_inside(self.p1,self.p2,Point(other.p2.x,other.p1.y)):
                return True
        if Rectangle.is_on_edge(other.p1,other.p2,self.p1,self.p2):
                return True
        return False

def find_intesections(arr):
    rectangles=[]
    intersections=[False]*len(arr)
    for r in arr:
        rectangles.append(Rectangle(Point(r[0],r[1]),Point(r[2],r[3])))

    for i in range(len(rectangles)):
        if intersections[i]:
            continue
        for n in range(len(rectangles)):
            if i==n:
                continue
            if rectangles[i].is_intersect(rectangles[n]):
                intersections[i],intersections[n]=True,True
    return intersections

#def main():
  #  write(find_intesections(read()))

#main()

def main_decorator(func_to_decorate):
       def the_wrapper_around_the_original_function():
           write(func_to_decorate(read()))
           return the_wrapper_around_the_original_function()

@main_decorator(find_intesections)
def dmain():
    return 0
   
#dmain=main_decorator(find_intesections)
dmain()