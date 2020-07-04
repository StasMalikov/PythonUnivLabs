from PyQt5 import QtCore
from PyQt5 import QtWidgets
import sys,MainForm
import Logic


class CellBtn(QtWidgets.QPushButton):
    def __init__(self,parent=None,color=None,text=None):
        QtWidgets.QPushButton.__init__(self,parent)
        self.color=color
        self.setFixedWidth(100)
        self.setFixedHeight(100)
        self.setText(text)#?????
        self.set_color()

    def set_color(self):
        if self.color=="red":
            self.setStyleSheet("background-color: #FF0000")

        if self.color=="yellow":
            self.setStyleSheet("background-color: #FFFF00")

        if self.color=="green":
            self.setStyleSheet("background-color: #00FF00")

        if self.color=="purple":
            self.setStyleSheet("background-color: #FF00FF")

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

class MyMainWindow(QtWidgets.QMainWindow,MainForm.Ui_MainWindow):
    def __init__(self, parent = None,game=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.game=game
        self.Lvl_label.setText("Level: %d" % game.level)

    def set_grid(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                tmp=CellBtn(None,matrix[i][j].color,matrix[i][j].text)
                self.gridLayoutWidget.addWidget(tmp,i,j)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Z :
            self.game.anti_clockwise_rotation()
            self.set_grid(self.game.matrix)
        if event.key() == QtCore.Qt.Key_X :
            self.game.clockwise_rotation()
            self.set_grid(self.game.matrix)
        if event.key() == QtCore.Qt.Key_I :#up
            if self.game.up()==True:
                self.game.grid.y-=1
                self.game.clear_grid_on_cells()
                self.game.set_grid_on_cells()
                self.set_grid(self.game.matrix)
        if event.key() == QtCore.Qt.Key_K :#down
            if self.game.down()==True:
                self.game.grid.y+=1
                self.game.clear_grid_on_cells()
                self.game.set_grid_on_cells()
                self.set_grid(self.game.matrix)
        if event.key() == QtCore.Qt.Key_J :#left
            if self.game.left()==True:
                self.game.grid.x-=1
                self.game.clear_grid_on_cells()
                self.game.set_grid_on_cells()
                self.set_grid(self.game.matrix)
        if event.key() == QtCore.Qt.Key_L :#right
            if self.game.right()==True:
                self.game.grid.x+=1
                self.game.clear_grid_on_cells()
                self.game.set_grid_on_cells()
                self.set_grid(self.game.matrix)
        self.moves_label.setText("Moves: %d" % self.game.moves)
        self.turns_label.setText("Turns: %d" % self.game.turns)
        self.rows_label.setText("Rows: %d/5" % self.game.rows)
        if self.game.check_win()==-1:
            dialog=QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon,"Game","You are complete this level!",buttons=QtWidgets.QMessageBox.Ok,parent=self)
            dialog.exec()
            self.on_clicked_up()

    def on_clicked_up(self):
        if self.game.max_lvl>self.game.level:
            self.game.level+=1
            self.game.load_lvl()
            self.game.clear_grid_on_cells()
            self.game.grid.x=1
            self.game.grid.y=1
            self.game.set_grid_on_cells()
            self.set_grid(self.game.matrix)
            self.Lvl_label.setText("Level: %d" % self.game.level)

class GameProcess:
    def __init__(self):
        self.game=Logic.GameLogic()
        self.window=MyMainWindow(None,self.game)
        self.set_signals()
        self.menu_signals()

    def set_signals(self):
        self.window.Up_Button.clicked.connect(self.on_clicked_up)
        self.window.Down_Button.clicked.connect(self.on_clicked_down)
        self.window.RestartButton.clicked.connect(self.on_clicked_restart)
        self.window.set_grid(self.game.matrix)

    def menu_signals(self):
        tAction=QtWidgets.QAction("Tools",self.window)
        hAction=QtWidgets.QAction("Help",self.window)
        tAction.triggered.connect(self.on_clicked_tools)
        hAction.triggered.connect(self.on_clicked_help)
        self.window.fileMenu.addAction(tAction)
        self.window.fileMenu.addAction(hAction)

    def on_clicked_tools(self):
        dialog=ToolsDialog()
        dialog.wNum.setText(str(self.window.width()))
        dialog.hNum.setText(str(self.window.height()))
        dialog.btn.clicked.connect(lambda : self.change_form(dialog))
        dialog.exec()

    def change_form(self,dialog=None):
        self.window.resize(int(dialog.wNum.text()),int(dialog.hNum.text()))


    def on_clicked_help(self):
        dialog=QtWidgets.QMessageBox(QtWidgets.QMessageBox.NoIcon,"Game Help","Задача: собрать кубики одного цвета в вертикальные линии;\n Как играть в Квадротека: стрелками клавиатуры двигается белый квадратный каркас, клавишами 'Х' и 'Z' вращение этого каркаса с кубиками по и против часовой стрелок.\n Shuffle - перемешать кубики",buttons=QtWidgets.QMessageBox.Ok,parent=self.window)
        dialog.exec()

    def on_clicked_up(self):
        if self.game.max_lvl>self.game.level:
            self.game.level+=1
            self.game.load_lvl()
            self.game.clear_grid_on_cells()
            self.game.grid.x=1
            self.game.grid.y=1
            self.game.set_grid_on_cells()
            self.window.set_grid(self.game.matrix)
            self.window.Lvl_label.setText("Level: %d" % self.game.level)
        

    def on_clicked_down(self):
        if self.game.min_lvl<self.game.level:
            self.game.level-=1
            self.game.load_lvl()
            self.game.clear_grid_on_cells()
            self.game.grid.x=1
            self.game.grid.y=1
            self.game.set_grid_on_cells()
            self.window.set_grid(self.game.matrix)
            self.window.Lvl_label.setText("Level: %d" % self.game.level)

    def on_clicked_restart(self):
        self.game.load_lvl()
        self.game.clear_grid_on_cells()
        self.game.grid.x=1
        self.game.grid.y=1
        self.game.set_grid_on_cells()
        self.window.set_grid(self.game.matrix)




if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    gp=GameProcess()
    gp.window.show()
    sys.exit(app.exec_())