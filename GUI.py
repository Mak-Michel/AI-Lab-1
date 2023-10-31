from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from answerManager import AnswerManager
from State import State

import sys

class GUI(QMainWindow):

    def __init__(self, manager: AnswerManager):
        super().__init__()
        self.__manager = manager

        self.setWindowTitle("Goal to Path")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        self.labels = []
        stateList = self.__manager.currStateList()
        for row in range(3):
            row_labels = []
            for col in range(3):
                label = QLabel(stateList[row][col])
                label.setAlignment(Qt.AlignCenter)  # Center the label
                label.setStyleSheet("background-color: CornflowerBlue; color: white; font-family: Comic Sans MS; font-size: 40px;")
                layout.addWidget(label, row, col)
                row_labels.append(label)
            self.labels.append(row_labels)

        button1 = QPushButton("Next")
        button2 = QPushButton("Prev")
        layout.addWidget(button2, 4, 0, 1, 1, Qt.AlignLeft)
        layout.addWidget(button1, 4, 2, 1, 1, Qt.AlignRight)

        button1.setStyleSheet("background-color: MediumBlue; color: white; font-family: Comic Sans MS")
        button2.setStyleSheet("background-color: MediumBlue; color: white; font-family: Comic Sans MS")

        button1.clicked.connect(self.next)
        button2.clicked.connect(self.prev)

        central_widget.setLayout(layout)

        # Display the initial state
        self.update_labels()

    def next(self):
        if self.__manager.nextState():
            self.update_labels()
        # ------------------------ ADD ELSE ERROR MESSAGE ----------------------------

    def prev(self):
        if self.__manager.prevState():
            self.update_labels()
        # ------------------------ ADD ELSE ERROR MESSAGE ----------------------------


    def update_labels(self):
        state_list = self.__manager.currStateList()
        for row in range(3):
            for col in range(3):
                self.labels[row][col].setText(state_list[row][col])
