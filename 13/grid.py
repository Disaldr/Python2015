import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Форма")
layout = QGridLayout()

layout.addWidget(QPushButton('0 0'), 0, 0)
layout.addWidget(QPushButton('0 1'), 0, 1)
layout.addWidget(QPushButton('0 2'), 0, 2)
layout.addWidget(QPushButton('1 0'), 1, 0)
layout.addWidget(QPushButton('1 1'), 1, 1)
layout.addWidget(QPushButton('1 2'), 1, 2)
layout.addWidget(QPushButton('2 0'), 2, 0)
layout.addWidget(QPushButton('2 1'), 2, 1)
layout.addWidget(QPushButton('2 2'), 2, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())