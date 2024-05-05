from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from exercise_page import ExercisePage

class MainWindow(QWidget):
    

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sağlık Takip Uygulaması")
        self.setGeometry(200, 200, 400, 250)

        self.person_height = 0
        self.person_weight = 0
        self.person_age = 0
        self.person_gender = ''
        self.person_endex = 0

        self.exercise_page = None
        
        self.height_label = QLabel("Boy (cm):", self)
        self.height_label.move(50, 30)
        self.height_input = QLineEdit(self)
        self.height_input.move(150, 30)
        
        self.weight_label = QLabel("Kilo (kg):", self)
        self.weight_label.move(50, 70)
        self.weight_input = QLineEdit(self)
        self.weight_input.move(150, 70)
        
        self.age_label = QLabel("Yaş:", self)
        self.age_label.move(50, 110)
        self.age_input = QLineEdit(self)
        self.age_input.move(150, 110)

        self.gender_label = QLabel("Cinsiyet:", self)
        self.gender_label.move(50, 150)
        self.gender_input = QLineEdit(self)
        self.gender_input.move(150, 150)
        
        self.calculate_button = QPushButton("Endeks Hesapla", self)
        self.calculate_button.move(150, 190)
        self.calculate_button.clicked.connect(self.calculate_bmi)
        
        self.show_exercise_button = QPushButton("Egzersizler", self)
        self.show_exercise_button.move(250, 190)
        self.show_exercise_button.clicked.connect(self.show_exercise)
        self.show_exercise_button.setEnabled(False)

    def calculate_bmi(self):
        self.person_height = float(self.height_input.text()) / 100  # cm to meters
        self.person_weight = float(self.weight_input.text())
        self.person_age = int(self.age_input.text())
        self.person_gender = self.gender_input.text()  # Cinsiyeti kullanıcıdan al
        
        self.person_endex = self.person_weight / (self.person_height ** 2)
        
        QMessageBox.information(self, "Endeks Bilgisi", f"Endeksiniz: {self.person_endex:.2f}\nCinsiyetiniz: {self.person_gender}")

        self.show_exercise_button.setEnabled(True)
    
    def show_exercise(self):
        try:
            yuruyus_miktar = 0
            kosu_miktar = 0
            yuzme_miktar = 0

            if self.person_endex < 18:
                yuruyus_miktar = 40
                kosu_miktar = 30
                yuzme_miktar = 30
            
            if 18.5 <= self.person_endex <= 24.0:
                yuruyus_miktar = 50
                kosu_miktar = 30
                yuzme_miktar = 20

            if 25 <= self.person_endex <= 29.9:
                yuruyus_miktar = 30
                kosu_miktar = 40
                yuzme_miktar = 30

            
            if  30 <= self.person_endex <= 34.9:
                yuruyus_miktar = 20
                kosu_miktar = 40
                yuzme_miktar = 40

            
            if 35 <= self.person_endex <= 39.9:
                yuruyus_miktar = 10
                kosu_miktar = 30
                yuzme_miktar = 60

            if self.person_endex > 40:
                yuruyus_miktar = 20
                kosu_miktar = 0
                yuzme_miktar = 80




            self.exercise_page = ExercisePage({"Yürüyüş": yuruyus_miktar, "Koşu": kosu_miktar , "Yüzme": yuzme_miktar})
            self.exercise_page.show()
        except Exception as e:
            print("sayfa açılmadı ", e)
        
