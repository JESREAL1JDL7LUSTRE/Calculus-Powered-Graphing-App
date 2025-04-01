from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication([])

with open("test.qss", "r") as file:
    app.setStyleSheet(file.read())

window = QWidget()
window.resize(200, 150)  # Set window size properly

layout = QVBoxLayout()

button = QPushButton("Click Me")
button.setFixedSize(100, 40)  # Set button size properly
layout.addWidget(button)

window.setLayout(layout)
window.show()

app.exec()
