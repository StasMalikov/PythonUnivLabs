class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Cell:
    def __init__(self,color,text):
        self.color=color
        self.text=text
        
  
class GameLogic:
    def __init__(self):
         self.grid=Point(1,1)#левывй верхний край решётки
         self.level=1
         self.load_lvl()
         self.set_grid_on_cells()
         self.turns=0
         self.moves=0
         self.rows=0

    def set_grid_on_cells(self):#рисуем решётку на ячейках
        j=self.grid.x
        i=self.grid.y
        self.matrix[i][j].text="o"
        self.matrix[i+1][j].text="|"
        self.matrix[i+2][j].text="o"
        self.matrix[i][j+1].text="---"
        self.matrix[i+2][j+1].text="---"
        self.matrix[i][j+2].text="o"
        self.matrix[i+1][j+2].text="|"
        self.matrix[i+2][j+2].text="o"

    def clear_grid_on_cells(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].text=""

    def clockwise_rotation(self):#по часовой стрелке
        j=self.grid.x
        i=self.grid.y
        #self.matrix[i][j].color,self.matrix[i][j+1].color,self.matrix[i][j+2].color,self.matrix[i+1][j].color,self.matrix[i+1][j+2].color,self.matrix[i+2][j].color,self.matrix[i+2][j+1].color,self.matrix[i+2][j+2].color=self.matrix[i+2][j].color,self.matrix[i+1][j].color,self.matrix[i][j].color,self.matrix[i+2][j+1].color,self.matrix[i][j+2].color,self.matrix[i+2][j+2].color,self.matrix[i+1][j+2].color,self.matrix[i][j+2].color
        #transponiruem
        self.matrix[i][j+1].color,self.matrix[i+1][j].color=self.matrix[i+1][j].color,self.matrix[i][j+1].color
        self.matrix[i][j+2].color,self.matrix[i+2][j].color=self.matrix[i+2][j].color,self.matrix[i][j+2].color
        self.matrix[i+1][j+2].color,self.matrix[i+2][j+1].color=self.matrix[i+2][j+1].color,self.matrix[i+1][j+2].color
        #obrashaem
        self.matrix[i][j].color,self.matrix[i][j+2].color=self.matrix[i][j+2].color,self.matrix[i][j].color
        self.matrix[i+1][j].color,self.matrix[i+1][j+2].color=self.matrix[i+2][j+1].color,self.matrix[i+1][j].color
        self.matrix[i+2][j].color,self.matrix[i+2][j+2].color=self.matrix[i+2][j+2].color,self.matrix[i+2][j].color
        self.turns+=1

    def anti_clockwise_rotation(self):#против часовой стрелки
        j=self.grid.x
        i=self.grid.y
        #obrashaem
        self.matrix[i][j].color,self.matrix[i][j+2].color=self.matrix[i][j+2].color,self.matrix[i][j].color
        self.matrix[i+1][j].color,self.matrix[i+1][j+2].color=self.matrix[i+2][j+1].color,self.matrix[i+1][j].color
        self.matrix[i+2][j].color,self.matrix[i+2][j+2].color=self.matrix[i+2][j+2].color,self.matrix[i+2][j].color
        #transponiruem
        self.matrix[i][j+1].color,self.matrix[i+1][j].color=self.matrix[i+1][j].color,self.matrix[i][j+1].color
        self.matrix[i][j+2].color,self.matrix[i+2][j].color=self.matrix[i+2][j].color,self.matrix[i][j+2].color
        self.matrix[i+1][j+2].color,self.matrix[i+2][j+1].color=self.matrix[i+2][j+1].color,self.matrix[i+1][j+2].color
        self.turns+=1


    def up(self):
        if self.grid.y==1 or self.grid.y==2:
            self.moves+=1
            return True
        else:
            return False

    def down(self):
        if self.grid.y==0 or self.grid.y==1:
            self.moves+=1
            return True
        else:
            return False

    def left(self):
        if self.grid.x==1 or self.grid.x==2:
            self.moves+=1
            return True
        else:
            return False

    def right(self):
        if self.grid.x==0 or self.grid.x==1:
            self.moves+=1
            return True
        else:
            return False

    def check_win(self):#проверка победы
        key=0
        self.rows=0
        for i in range(len(self.matrix)):
            tmp_color= self.matrix[0][i].color
            for j in range(len(self.matrix)):
                if self.matrix[j][i].color==tmp_color:
                    key+=1
            
            if key==5:
                self.rows+=1
            key=0

        if self.rows==5:
            return -1    #победа
        else:
            return 0    #пока не победа
    
    def load_lvl(self):#загружаем новую матрицу ячеек
        self.matrix=self.init_matrix(GameLogic.Levels(self.level))

    def init_matrix(self,arr):#инициализируем новую матрицу ячеек
        result=[]
        for i in range(len(arr)):
            result.append([])
            for j in range(len(arr)):
                result[i].append(Cell(arr[i][j],""))
        return result

    @property
    def max_lvl(self):
        return 3

    @property
    def min_lvl(self):
        return 1

    def Levels(num):#уровни игры
        if num==1:
            return [["red","yellow","red","red","red"],["red","yellow","yellow","yellow","red"],["red","red","red","red","red"],["red","red","red","red","red"],["red","yellow","red","red","red"]]
            #return [["red","red","yellow","yellow","red"],["red","yellow","yellow","red","red"],["yellow","red","red","yellow","red"],["red","yellow","yellow","red","red"],["yellow","red","red","yellow","red"]]
        if num==2:
            return [["yellow","red","green","red","yellow"],["red","yellow","red","red","yellow"],["green","yellow","red","red","yellow"],["red","green","red","yellow","yellow"],["red","red","yellow","yellow","green"]]
        if num==3:
            return [["green","red","yellow","purple","red"],["red","green","purple","yellow","red"],["red","yellow","purple","green","red"],["red","green","red","purple","yellow"],["red","red","yellow","green","purple"]]
        #[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]

