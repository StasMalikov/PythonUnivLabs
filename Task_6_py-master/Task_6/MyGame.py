class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Cell:
    def __init__(self,num,pt,is_swapped):
        self.num=num
        self.point=pt
        self.is_swapped=is_swapped

class Game:

    def __init__(self):
       self.level=1
       self.load_lvl()
       self.shift_points=[]

    def load_lvl(self):
        self.matrix=self.init_matrix(Game.Levels(self.level))

    def change(self,cb,cb0):
        c=self.matrix[cb.x][cb.y]
        c0=self.matrix[cb0.x][cb0.y]
        c.num,c0.num=c0.num,c.num
        c0.point.x,c.point.x=c.point.x,c0.point.x
        c0.point.y,c.point.y=c.point.y,c0.point.y
        c.is_swapped=False
        c0.is_swapped=True

    def check_win(self):
        key=0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j].num>0 and self.matrix[i][j].is_swapped==False:
                    key+=1
        if key==0:
            return 1
        else:
            return 0

    #                   формируем массив координат для передвижения ячейки
    def show_moves(self,x,y):
        cell=self.matrix[x][y]
        result=[]
        
        #вверх
        if cell.point.y-cell.num>=0 and self.matrix[cell.point.x][cell.point.y-cell.num].num==0:
            result.append(Point(cell.point.x,cell.point.y-cell.num))

        #вниз
        if cell.point.y+cell.num<len(self.matrix) and self.matrix[cell.point.x][cell.point.y+cell.num].num==0:
            result.append(Point(cell.point.x,cell.point.y+cell.num))

        #влево
        if cell.point.x-cell.num>=0 and self.matrix[cell.point.x-cell.num][cell.point.y].num==0:
            result.append(Point(cell.point.x-cell.num,cell.point.y))

        #вправо
        if cell.point.x+cell.num<len(self.matrix) and self.matrix[cell.point.x+cell.num][cell.point.y].num==0:
            result.append(Point(cell.point.x+cell.num,cell.point.y))

        #вверх-вправо
        if cell.point.x+cell.num<len(self.matrix) and cell.point.y-cell.num>=0 and self.matrix[cell.point.x+cell.num][cell.point.y-cell.num].num==0:
            result.append(Point(cell.point.x+cell.num,cell.point.y-cell.num))
        #вверх-влево
        if cell.point.x-cell.num>=0 and cell.point.y-cell.num>=0 and self.matrix[cell.point.x-cell.num][cell.point.y-cell.num].num==0:
            result.append(Point(cell.point.x-cell.num,cell.point.y-cell.num))
        #вниз-вправо
        if cell.point.x+cell.num<len(self.matrix) and cell.point.y+cell.num<len(self.matrix)and self.matrix[cell.point.x+cell.num][cell.point.y+cell.num].num==0:
            result.append(Point(cell.point.x+cell.num,cell.point.y+cell.num))
        #вниз-влево
        if cell.point.x-cell.num>=0 and cell.point.y+cell.num<len(self.matrix)and self.matrix[cell.point.x-cell.num][cell.point.y+cell.num].num==0:
            result.append(Point(cell.point.x-cell.num,cell.point.y+cell.num))

        return result
        
    def init_matrix(self,arr):
        result=[]
        for i in range(len(arr)):
            result.append([])
            for j in range(len(arr)):
                result[i].append(Cell(arr[i][j],Point(i,j),False))
        return result
    @property
    def max_lvl(self):
        return 3

    @property
    def min_lvl(self):
        return 1


    def Levels(num):
        if num==1:
            #return  [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,2,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
            return [[0,0,0,0,0,0],[3,2,3,2,2,2],[0,0,2,3,2,2],[2,0,2,2,0,0],[0,2,3,0,2,2],[2,3,0,2,0,4]]
        if num==2:
            return [[0,2,3,3,2,1],[2,0,3,3,0,2],[1,4,3,3,0,1],[1,4,3,3,0,1],[2,0,3,3,0,2],[0,2,3,3,2,1]]
        if num==3:
            return [[0,2,2,2,0,2],[1,1,1,1,1,1],[1,3,0,3,3,1],[1,3,3,3,3,1],[1,1,1,1,1,1],[4,4,0,4,0,1]]