import os
import platform
import subprocess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QSpinBox,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QHeaderView,
)
from About import AboutWindow


class GradesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""
        self.header = ""
        self.about_window = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grades Correction")
        self.setGeometry(100, 100, 700, 600)

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

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)

        bottom_bar = QHBoxLayout()

        self.bonus_spinbox = QSpinBox()
        self.bonus_spinbox.setRange(0, 100)
        self.bonus_spinbox.lineEdit().returnPressed.connect(self.apply_bonus)

        self.update_button = QPushButton("Update File")
        self.update_button.setObjectName("updateButton")
        self.update_button.clicked.connect(self.update_file)

        bottom_bar.addWidget(self.bonus_spinbox)
        bottom_bar.addWidget(self.update_button)
        main_layout.addLayout(bottom_bar)

        self.setLayout(main_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "CSV Files (*.csv)"
        )
        self.selected_file = file_path

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(self.selected_file, "r") as f:
            self.header = f.readline()
            for line in f:
                parts = line.split(",")
                student_id = parts[0].strip()
                grade = int(parts[1])
                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)

        self.update_table()

    def update_table(self):
        self.table.clearContents()

        for row in range(len(self.student_ids)):
            id_item = QTableWidgetItem(str(self.student_ids[row]))
            orig_item = QTableWidgetItem(str(self.original_grades[row]))
            corr_item = QTableWidgetItem(str(self.corrected_grades[row]))

            id_item.setTextAlignment(Qt.AlignCenter)
            orig_item.setTextAlignment(Qt.AlignCenter)
            corr_item.setTextAlignment(Qt.AlignCenter)

            self.table.setItem(row, 0, id_item)
            self.table.setItem(row, 1, orig_item)
            self.table.setItem(row, 2, corr_item)

    def apply_bonus(self):
        self.bonus_spinbox.interpretText()
        bonus = self.bonus_spinbox.value()

        for i in range(len(self.original_grades)):
            new_grade = self.original_grades[i] + bonus
            if new_grade > 100:
                new_grade = 100
            self.corrected_grades[i] = new_grade

        self.update_table()

    def update_file(self):
        with open(self.selected_file, "w") as f:
            f.write(self.header)
            for i in range(len(self.student_ids)):
                f.write(f"{self.student_ids[i]},{self.corrected_grades[i]}\n")

        self.open_file(self.selected_file)

    def open_file(self, file_path):
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", file_path])
        else:
            subprocess.Popen(["xdg-open", file_path])

    def open_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    window = GradesWindow()
    window.show()
    app.exec()
