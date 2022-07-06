from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea,
                             QLineEdit, QFormLayout, QHBoxLayout, QFrame,
                             QPushButton, QLabel, QListWidget, QDialog, QAction, QToolBar)
from PyQt5.QtCore import Qt


from manager import (get_all_entries, search_website, register_website,
                     delete_entry)
                     
class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__()

class CustomFrame(QFrame):
    def __init__(self, datas):
        super().__init__()
       

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
def main():
    app = QApplication([])
    app.setStyle('fusion')
    win = Main()
    win.show()
    app.exec_()


if __name__ == '__main__':
    main()
