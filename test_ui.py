
from PyQt5 import QtWidgets, uic
from akinator import CantGoBackAnyFurther, InvalidAnswer, Akinator, Answer, Theme


class Akinator:
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/inicio.ui")
        self.tl = uic.loadUi("telas/pergunta1.ui")
        self.tela_inicial.show()
        
        self.tela_inicial.btIniciar.clicked.connect(self.abrir)
        app.exec()
        
    def abrir(self):
        self.tela_inicial.close()
        self.tl.show()
        
        
akinator_gui = Akinator()