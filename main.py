import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from components.interface.home import Home
from components.interface.home_controller import HomeController
app = QApplication(sys.argv)

with open("main.qss", "r") as file:
    app.setStyleSheet(file.read())
    
window = QMainWindow()
window.resize(1726, 777)
window.setWindowTitle("Calculus Tool")

home = Home()
controller = HomeController(home)
home.set_controller(controller)
window.setCentralWidget(home)
window.show()

# Launch the application
app.exec()