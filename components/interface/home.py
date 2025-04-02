import sys
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout 
from components.logic.magic import Magic

class Home:
    def __init__(self):
        self.launch_home()

    def launch_home(self):
        magic_instance = Magic()
        derivative_result, integral_result = magic_instance.magic_func()
        print(f"Derivative: {derivative_result}")
        print(f"Integral: {integral_result}")
        
        with open("components/interface/home.qss", "r") as file:
            self.setStyleSheet(file.read())