import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from components.interface.home import Home

app = QApplication(sys.argv)

with open("main.qss", "r") as file:
    app.setStyleSheet(file.read())
    
window = QMainWindow()
window.resize(600, 800)
window.setWindowTitle("My Application")


launch_home = Home()
window.show()

# Launch the application
app.exec()