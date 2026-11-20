import os
import platform
import subprocess
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QSpinBox,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
    QHeaderView,
    QAbstractItemView,
)
from About import AboutWindow


class GradesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""

        self.header_line = "ID,Grade"
        self.delimiter = ","
        self.about_window = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grades Correction Tool")
        self.setGeometry(100, 100, 720, 620)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(14)

        self.title_label = QLabel("Student Grades Correction")
        self.title_label.setObjectName("titleLabel")
        main_layout.addWidget(self.title_label)

        top_bar = QHBoxLayout()
        top_bar.setSpacing(10)

        self.load_button = QPushButton("Load Grades File")
        self.load_button.clicked.connect(self.load_file)

        self.file_label = QLabel("No file selected")
        self.file_label.setObjectName("fileLabel")

        self.about_button = QPushButton("About")
        self.about_button.setObjectName("aboutButton")
        self.about_button.clicked.connect(self.open_about)

        top_bar.addWidget(self.load_button)
        top_bar.addWidget(self.file_label, 1)
        top_bar.addWidget(self.about_button)
        main_layout.addLayout(top_bar)

        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        main_layout.addWidget(self.table, 1)

        bottom_bar = QHBoxLayout()
        bottom_bar.setSpacing(12)

        self.bonus_label = QLabel("Bonus Points (press Enter):")
        self.bonus_label.setObjectName("sectionLabel")

        self.bonus_spinbox = QSpinBox()
        self.bonus_spinbox.setRange(0, 100)
        self.bonus_spinbox.setValue(0)
        self.bonus_spinbox.lineEdit().returnPressed.connect(self.apply_bonus)

        self.update_button = QPushButton("Update File")
        self.update_button.setObjectName("updateButton")
        self.update_button.clicked.connect(self.update_file)

        bottom_bar.addWidget(self.bonus_label)
        bottom_bar.addWidget(self.bonus_spinbox)
        bottom_bar.addStretch()
        bottom_bar.addWidget(self.update_button)
        main_layout.addLayout(bottom_bar)

        self.setLayout(main_layout)

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Grades File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if not file_path:
            return

        self.selected_file = file_path
        self.file_label.setText(os.path.basename(file_path))

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(self.selected_file, "r", encoding="utf-8-sig") as f:
            first_line = f.readline()
            self.header_line = first_line.strip()
            self.delimiter = ", " if ", " in self.header_line else ","

            for line in f:
                clean_line = line.strip()
                if not clean_line:
                    continue
                parts = clean_line.split(",")
                student_id = parts[0].strip()
                grade_str = parts[1].strip()
                if "." in grade_str:
                    grade = float(grade_str)
                else:
                    grade = int(grade_str)

                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)

        self.bonus_spinbox.setValue(0)
        self.update_table()

    def update_table(self):
        row_count = max(50, len(self.student_ids))
        self.table.setRowCount(row_count)
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
        if not self.selected_file:
            QMessageBox.warning(self, "No File Selected", "Please load a grades file first.")
            return

        with open(self.selected_file, "w", encoding="utf-8") as f:
            f.write(f"{self.header_line}\n")
            for i in range(len(self.student_ids)):
                f.write(f"{self.student_ids[i]}{self.delimiter}{self.corrected_grades[i]}\n")

        self.open_file_all_os(self.selected_file)

    def open_file_all_os(self, file_path):
        system_name = platform.system()
        if system_name == "Windows":
            os.startfile(file_path)
        elif system_name == "Darwin":
            subprocess.Popen(["open", file_path])
        else:
            subprocess.Popen(["xdg-open", file_path])

    def open_about(self):
        if self.about_window is None:
            self.about_window = AboutWindow()
        self.about_window.show()
        self.about_window.raise_()


def load_stylesheet(app):
    qss_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())


if __name__ == "__main__":
    app = QApplication()
    load_stylesheet(app)
    window = GradesWindow()
    window.show()
    app.exec()
