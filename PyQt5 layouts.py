# PyQt5 layouts
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QVBoxLayout,
                             QWidget,QHBoxLayout,QGridLayout,QLabel)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color:red")
        label2.setStyleSheet("background-color:yellow")
        label3.setStyleSheet("background-color:green")
        label4.setStyleSheet("background-color:blue")
        label5.setStyleSheet("background-color:purple")

        grid = QGridLayout()

        grid.addWidget(label1, 0,0,)
        grid.addWidget(label2,  0, 1)
        grid.addWidget(label3, 1,0)
        grid.addWidget(label4, 1,1)
        grid.addWidget(label5, 1,2)

        central_widget.setLayout(grid)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
