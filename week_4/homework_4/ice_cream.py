import os
import numpy as np
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
)
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)
from matplotlib.figure import Figure
from About import AboutWindow


class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []
        self.about_window = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ice Cream Sales")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        top_bar = QHBoxLayout()

        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("aboutButton")
        self.about_button.clicked.connect(self.open_about)

        top_bar.addWidget(self.load_button)
        top_bar.addWidget(self.about_button)
        main_layout.addLayout(top_bar)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.toolbar = NavigationToolbar(self.canvas, self)

        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "CSV Files (*.csv)"
        )

        self.temperatures = []
        self.revenues = []

        with open(file_path, "r") as f:
            next(f)
            for line in f:
                parts = line.split(",")
                self.temperatures.append(float(parts[0]))
                self.revenues.append(float(parts[1]))

        self.plot_graph()

    def plot_graph(self):
        self.ax.clear()

        self.ax.scatter(self.temperatures, self.revenues, s=1)

        m, b = np.polyfit(self.temperatures, self.revenues, 1)
        x_line = np.array([min(self.temperatures), max(self.temperatures)])
        y_line = m * x_line + b
        self.ax.plot(x_line, y_line, color="red", label=f"y = {m:.2f}x + {b:.2f}")

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_title("Ice Cream Revenue vs Temperature")
        self.ax.set_xlabel("Temperature")
        self.ax.set_ylabel("Revenue ($)")
        self.ax.legend()

        self.canvas.draw()

    def open_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    window = IceCreamWindow()
    window.show()
    app.exec()
