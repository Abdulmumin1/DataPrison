from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea,
                             QLineEdit, QFormLayout, QHBoxLayout, QFrame,
                             QPushButton, QLabel, QListWidget, QDialog, QAction, QToolBar)
from PyQt5.QtCore import Qt


from manager import (get_all_entries, search_website, register_website,
                     delete_entry)
from genp import generate_password

colors = {
    'cover': '#101019',
    'primary': "#181825",
    'secondary': "#e8a202",
    "white": "#fff"
}

scroll_var = """QScrollBar::vertical{width:6px;}
        QScrollBar::handle:vertical{background:#181825; opacity:.3; min-height:0px;}
        QScrollBar::handle:vertical:active{background:#e8a202; border-radius:5px;}
        QScrollBar::add-line:vertical{height:0px; subcontrol-position:bottom;}
        QScrollBar::sub-line:vertical{height:0px; subcontrol-position:top;}
        """
scroll_hor = """QScrollBar::horizontal{height:6px;}
        QScrollBar::handle:horizontal{background:#181825; min-height:0px;}
        QScrollBar::handle:horizontal:active{background:#e8a202; border-radius:5px;}
        QScrollBar::add-line:horizontal{height:0px; subcontrol-position:bottom;}
        QScrollBar::sub-line:horizontal{height:0px; subcontrol-position:top;}
        """


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle('Create new')

        dlg_layout = QVBoxLayout()

        formLayout = QFormLayout()

        self.website = QLineEdit()
        self.password = QLineEdit()
        self.email = QLineEdit()

        formLayout.addRow('Website:', self.website)
        formLayout.addRow('Password:', self.password)
        formLayout.addRow('Email:', self.email)

        # genarate password button
        generate_password = self.create_button(
            "Generate password", self.generate_password_)
        btn_layout = QHBoxLayout()
        ok = self.create_button(text='Ok', func=self.register)
        cancel = self.create_button(text='Cancel', func=self.close)

        btn_layout.addWidget(ok)
        btn_layout.addWidget(cancel)

        dlg_layout.addLayout(formLayout)
        dlg_layout.addWidget(generate_password)
        dlg_layout.addLayout(btn_layout)

        self.setLayout(dlg_layout)

    def create_button(self, text, func):
        button = QPushButton(text=text, clicked=func)
        button.setStyleSheet('*{' + f'background:{colors["secondary"]};' +
                             f'border-radius:5px; padding:10px; color:{colors["primary"]};'+'}'
                             )
        return button

    def register(self):
        website_text = self.website.text()
        password_text = self.password.text()

        email_text = self.email.text()

        self.close()
        datas = register_website(website_text, password_text, email_text)
        card = CustomFrame(datas)

        self.parent().scroll_frame_layout.insertWidget(0, card)

    def closeEvent(self, event):
        self.parent().dialog = False

    def generate_password_(self):
        password = generate_password()
        self.password.setText(password)


class CustomFrame(QFrame):
    def __init__(self, datas):
        super().__init__()
        self.setStyleSheet(
            "QFrame{"+f"background:{colors['primary']}; padding:6px; border-radius:5px;"+"}")

        layout = QHBoxLayout()

        website = datas[0].capitalize()
        password = datas[1]
        password = password[:12]+'...' if len(password) > 12 else password
        # password_string = ''.join(['x' for x in range(len(password))])
        # password_string = password_string[:10]
        self.id = datas[2]

        label = QLabel(
            text=f"<h3>{website}</h3>")

        button_copy = self.create_button(
            '❐', lambda: QApplication.clipboard().setText(datas[1]))
        button_email = self.create_button(
            "✉", lambda: QApplication.clipboard().setText(datas[3]))
        button_delete = self.create_button('✗', self.delete_card)

        layout.addWidget(label)
        layout.addStretch(1)
        layout.addWidget(button_copy)
        layout.addWidget(button_email)
        layout.addWidget(button_delete)

        self.setLayout(layout)

    def create_button(self, text, func):
        button = QPushButton(text=text, clicked=func)
        button.setStyleSheet('*{' + f'max-height:30px;background:{colors["secondary"]};' +
                             f' border-radius:5px; padding:10px; color:{colors["primary"]};'+'}' +
                             '*:hover{background:#E6AF32}')
        return button

    def delete_card(self):

        delete_entry(self.id)
        self.close()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            f'background:{colors["cover"]}; color:{colors["secondary"]}')
        self.initUI()
        self.get_items()

    def initUI(self):
        self.dialog = False
        self.main_frame = QFrame()
        self.main_layout = QVBoxLayout(self.main_frame)

        self.search_field = QLineEdit()
        self.search_field.setPlaceholderText('Search here...')
        self.search_field.textChanged[str].connect(self.search_website)
        # toolbar

        self.toolbar = QToolBar()
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)

        create_action = QAction(self, text='Create')
        create_action.triggered.connect(self.register)

        self.toolbar.addAction(create_action)

        self.scroll_area()
        self.main_layout.addWidget(self.search_field)
        self.setCentralWidget(self.main_frame)

    def scroll_area(self):
        scroll_frame = QFrame()
        self.scroll_frame_layout = QVBoxLayout(scroll_frame)
        self.scroll_frame_layout.addStretch(1)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(scroll_frame)
        scroll.setStyleSheet('QScrollArea{border:0;}'+scroll_var+scroll_hor)

        self.main_layout.addWidget(scroll)

    def get_items(self):
        entries = get_all_entries()
        for entry in entries:
            card = CustomFrame(entry)
            self.scroll_frame_layout.insertWidget(0, card)

    def clear_layout(self):
        for i in range(self.scroll_frame_layout.count()-1):
            self.scroll_frame_layout.itemAt(i).widget().deleteLater()

    def search_website(self):
        self.clear_layout()

        query = self.search_field.text()
        result = search_website(query)
        if result:
            for res in result:
                card = CustomFrame(res)
                self.scroll_frame_layout.insertWidget(0, card)

    def register(self):
        if self.dialog:
            return
        dialog = Dialog(self)
        dialog.show()
        self.dialog = True


def main():
    app = QApplication([])
    win = Main()
    win.show()
    win.resize(460, 680)
    app.exec_()


if __name__ == '__main__':
    main()
