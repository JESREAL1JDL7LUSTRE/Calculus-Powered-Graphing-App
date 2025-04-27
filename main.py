import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from components.interface.home import Home
from components.interface.home_controller import HomeController
app = QApplication(sys.argv)

with open("main.qss", "r") as file:
    app.setStyleSheet(file.read())
    
window = QMainWindow()
window.resize(1417, 592)
window.setWindowTitle("My Application")

home = Home()
controller = HomeController(home)
home.set_controller(controller)
window.setCentralWidget(home)
window.show()

# Launch the application
app.exec()