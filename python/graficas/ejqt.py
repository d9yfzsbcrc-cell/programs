# Ejemplo conceptual (simplificado):
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import sys


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

# En tu ventana principal:
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = MplCanvas(self)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Graficar datos
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.canvas.axes.plot(x, y)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MiVentana()
    w.show()

    sys.exit(app.exec())
