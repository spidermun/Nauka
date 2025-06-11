# PyQt5 zdjecia
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moja pierwsze gui")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("Lottery_Slots.png"))

        label = QLabel(self)
        label.setGeometry(10,10,250,250)

        pixmap = QPixmap("Lottery_Slots.png")
        label.setPixmap(pixmap)
        # Ustawienie skalowania zawartości etykiety
        label.setScaledContents(True)
        # Ustawienie rozmiaru etykiety na rozmiar pixmapy
        label.setGeometry((self.width() - label.width()) // 2, # Wyśrodkowanie etykiety
                          (self.height() - label.height()) // 2,
                            label.width(),
                            label.height())



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()