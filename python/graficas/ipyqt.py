
# -*- coding: utf-8 -*-

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel

class AppContador(QWidget):
    def __init__(self):
        super().__init__()
        self.contador = 0

        self.setWindowTitle("Contador")
        self.setGeometry(100, 100, 300, 200)

        layout = QHBoxLayout()

        self.label = QLabel("0", self)
        self.label.setStyleSheet("font-size: 30px;")

        self.button = QPushButton("Incrementar", self)
        self.button.setStyleSheet("""
            font-size: 20px;
            border-radius: 20px;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border: 2px solid #3E8E41;
        """)

        self.button.clicked.connect(self.suma_contador)

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def suma_contador(self):
        self.contador += 1
        if self.contador == 100:
            self.label.setText("🎉")
            self.contador = 0
        else:
            self.label.setText(str(self.contador))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = AppContador()
    w.show()

    sys.exit(app.exec())