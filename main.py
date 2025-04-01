import sys
from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(600, 800)
window.setWindowTitle("My Application")
window.show()

# Launch the application
app.exec()