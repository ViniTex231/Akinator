from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, QObject
from iniciotela import Ui_Inicio
from test_sync import test
import time


class JanelaInicio(Ui_Inicio):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.btIniciar.clicked.connect(self.btn_click)
        self.worker = Worker()
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.started.connect(self.worker.do_work)
        

    def btn_click(self):
        self.worker_thread.start()
        
        
        
class Worker(QObject):
    def do_work(self):
        test()
        
    def StartAki(self):
        MainWindow.close()
            
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    janela = JanelaInicio(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
