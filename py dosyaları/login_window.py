from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal

class LoginWindow(QWidget):
    login_success = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Giriş")
        self.setGeometry(200, 200, 300, 150)
        
        self.username_label = QLabel("Kullanıcı Adı:", self)
        self.username_label.move(50, 30)
        self.username_input = QLineEdit(self)
        self.username_input.move(150, 30)
        
        self.password_label = QLabel("Şifre:", self)
        self.password_label.move(50, 70)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(150, 70)
        
        self.login_button = QPushButton("Giriş", self)
        self.login_button.move(150, 110)
        self.login_button.clicked.connect(self.check_credentials)
    
    def check_credentials(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        if username == "admin" and password == "admin":
            self.login_success.emit()
        else:
            QMessageBox.warning(self, "Hata", "Geçersiz kullanıcı adı veya şifre!")