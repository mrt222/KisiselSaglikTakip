import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login_window = LoginWindow()
    main_window = MainWindow()
    
    def show_main_window():
        login_window.hide()
        main_window.show()
    
    login_window.login_success.connect(show_main_window)
    
    login_window.show()
    
    sys.exit(app.exec_())

