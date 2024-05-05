from PyQt5.QtWidgets import *

class ExercisePage(QWidget):
    def __init__(self, exercises):
        super().__init__()
        self.setWindowTitle("Egzersizler")
        self.setGeometry(200, 200, 400, 300)
        
        self.exercises = exercises
        
        self.progressbars = []
        for i, (exercise_name, progress) in enumerate(exercises.items()):
            label = QLabel(exercise_name, self)
            label.move(50, 30 + i * 40)
            progressbar = QProgressBar(self)
            progressbar.setGeometry(150, 30 + i * 40, 200, 25)
            progressbar.setValue(progress)
            self.progressbars.append(progressbar)