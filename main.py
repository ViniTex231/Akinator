from PyQt5 import QtCore, QtGui, QtWidgets
from inicio import Ui_Inicio
from test_sync import test


class Janela(Ui_Inicio):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.btIniciar.clicked.connect(self.btn_click)

    def btn_click(self):
        test()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    janela = Janela(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
