from PyQt5 import QtWidgets
import sys,converted_form
import MyGame


class CellBtn(QtWidgets.QPushButton):
    def __init__(self,parent=None,cell=None,x=None,y=None):
        QtWidgets.QPushButton.__init__(self,parent)
        self.num=cell.num
        self.color="white"
        self.flag=cell.is_swapped
        self.pressed=False
        self.x=x
        self.y=y
        self.setFixedWidth(100)
        self.setFixedHeight(100)
        if self.num!=0:
            self.setText("%d" % self.num)
        self.set_color(self.num)

    def set_color(self,num):
        if num==0:
            self.setStyleSheet("background-color: #D3D3D3")
        if num==1:
            self.setStyleSheet("background-color: #FFA500")
        if num==2:
            self.setStyleSheet("background-color: #B22222")
        if num==3:
            self.setStyleSheet("background-color: #228B22")
        if num==4:
            self.setStyleSheet("background-color: #7B68EE")
        if self.flag==True:                                     #changed
            self.setStyleSheet("background-color: #696969")

class MyMainWindow(QtWidgets.QMainWindow,converted_form.Ui_MainWindow):
    def __init__(self, parent = None,game=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.Lvl_label.setText("Level: %d" % game.level)

    def set_grid(self,matrix,obj):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp=CellBtn(None,matrix[i][j],i,j)
                tmp.clicked.connect(obj.on_clicked_cell)
                if matrix[i][j].is_swapped:
                    tmp.flag=True
                    tmp.enabled=False
                self.gridLayoutWidget.addWidget(tmp,i,j)

    def set_moves(self,points,matrix,obj):
        for i in range(len(points)):
            tmp=CellBtn(None,matrix[points[i].x][points[i].y],points[i].x,points[i].y)
            tmp.clicked.connect(obj.on_clicked_cell)
            tmp.setText("x")
            self.gridLayoutWidget.addWidget(tmp,points[i].x,points[i].y)


class ToolsDialog(QtWidgets.QDialog):
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        wl= QtWidgets.QLabel()
        wl.setText("Set Form width")
        hl= QtWidgets.QLabel()
        hl.setText("Set Form height")
        self.wNum=QtWidgets.QLineEdit()
        self.hNum=QtWidgets.QLineEdit()
        self.btn=QtWidgets.QPushButton()
        self.btn.setText("Ok")
        vbox=QtWidgets.QVBoxLayout()
        vbox.addWidget(wl)
        vbox.addWidget(self.wNum)
        vbox.addWidget(hl)
        vbox.addWidget(self.hNum)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

class GameProcess:
    def __init__(self):
        self.game=MyGame.Game()
        self.window=MyMainWindow(None,self.game)
        self.set_signals()
        self.menu_signals()
        self.pressed_Cell=None
       
    def set_signals(self):
        self.window.Up_Button.clicked.connect(self.on_clicked_up)
        self.window.Down_Button.clicked.connect(self.on_clicked_down)
        self.window.RestartButton.clicked.connect(self.on_clicked_restart)
        self.window.set_grid(self.game.matrix,self)
        #self.window.HelpButton.clicked.connect(self.on_clicked_help)
        #self.window.ToolsButton.clicked.connect(self.on_clicked_tools)

    def menu_signals(self):
        tAction=QtWidgets.QAction("Tools",self.window)
        hAction=QtWidgets.QAction("Help",self.window)
        tAction.triggered.connect(self.on_clicked_tools)
        hAction.triggered.connect(self.on_clicked_help)
        self.window.fileMenu.addAction(tAction)
        self.window.fileMenu.addAction(hAction)

    def on_clicked_cell(self):                  #нажатие на ячейку
        sender=self.window.sender()
        if sender.num>0:              # не пустая ячейка
            if sender.flag==False:      #не перемещался
                if sender.pressed==False:      # ещё не нажат
                    self.pressed_Cell=sender
                    sender.pressed=True
                    self.window.set_grid(self.game.matrix,self)
                    sender.set_color(-1)
                    self.window.set_moves(self.game.show_moves(sender.x,sender.y),self.game.matrix,self) # ставим крестики
        else:
            if sender.text()=="x":
                self.game.change(self.pressed_Cell,sender)
                self.window.set_grid(self.game.matrix,self)
                if self.game.check_win()==1:
                    dialog=QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon,"Game","Вы прошли этот уровень!",buttons=QtWidgets.QMessageBox.Ok,parent=self.window)
                    dialog.exec()
                    self.on_clicked_up()
                
    def on_clicked_tools(self):
        dialog=ToolsDialog()
        dialog.wNum.setText(str(self.window.width()))
        dialog.hNum.setText(str(self.window.height()))
        dialog.btn.clicked.connect(lambda : self.change_form(dialog))
        dialog.exec()

    def change_form(self,dialog=None):
        self.window.resize(int(dialog.wNum.text()),int(dialog.hNum.text()))


    def on_clicked_help(self):
        dialog=QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon,"Game Help","Задача: сделать по одному ходу каждой фишкой. Длинна шага - число на фишке;\nКак играть в Цифровой кузнечик :\n Управление:\n кликаете мышкой на фишку и видите места куда можно сделать ход, они помечены крестиком, если есть доступные ходы для этой фишки.\n Начать уровень сначала - Restart.",buttons=QtWidgets.QMessageBox.Ok,parent=self.window)
        dialog.exec()

    def on_clicked_up(self):
        if self.game.max_lvl>self.game.level:
            self.game.level+=1
            self.game.load_lvl()
            self.window.set_grid(self.game.matrix,self)
            self.window.Lvl_label.setText("Level: %d" % self.game.level)
        

    def on_clicked_down(self):
        if self.game.min_lvl<self.game.level:
            self.game.level-=1
            self.game.load_lvl()
            self.window.set_grid(self.game.matrix,self)
            self.window.Lvl_label.setText("Level: %d" % self.game.level)

    def on_clicked_restart(self):
        self.game.load_lvl()
        self.window.set_grid(self.game.matrix,self)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    gp=GameProcess()
    gp.window.show()
    sys.exit(app.exec_())



