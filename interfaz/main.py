import sys, os, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

#Ventana de Inicio
class Inicio(QMainWindow):

    def __init__(self):
        super(Inicio, self).__init__()
        loadUi('interfaz/inicio.ui', self)
        
        self.btn_iniciar.clicked.connect(self.abrirDatos)

    def abrirDatos(self):
        otraVentana = Datos(self)
        otraVentana.show()

#Ventana para inigresar los datos de los jugadores 
class Datos(QMainWindow):
    def __init__(self, parent = None):
        super(Datos, self).__init__()
        loadUi('interfaz/datos.ui', self)
        self.btn_cancelar.clicked.connect(self.abrirVentanaPrincipal)

    def abrirVentanaPrincipal(self): 
        self.parent().show()
        self.close()

app = QApplication(sys.argv)
main = Inicio()
main.show()
sys.exit(app.exec_())