import sys
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout  # ✅ Correct


class Home(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        label = QLabel("Welcome to My Application!")
        layout.addWidget(label)

        self.setLayout(layout)
        
        with open("components/interface/home.qss", "r") as file:
            self.setStyleSheet(file.read())