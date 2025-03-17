import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class AddressBookApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.contacts = {}  # 이름과 전화번호를 저장할 딕셔너리

    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('주소록 프로그램')
        self.setGeometry(300, 300, 300, 200)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 이름과 전화번호 입력을 위한 텍스트 박스
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("이름 입력")
        layout.addWidget(self.name_input)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("전화번호 입력")
        layout.addWidget(self.phone_input)

        # 연락처 추가 버튼
        self.add_button = QPushButton("추가", self)
        self.add_button.clicked.connect(self.add_contact)
        layout.addWidget(self.add_button)

        # 이름으로 연락처를 찾을 수 있는 입력 박스
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("이름으로 찾기")
        layout.addWidget(self.search_input)

        # 찾기 버튼
        self.search_button = QPushButton("찾기", self)
        self.search_button.clicked.connect(self.search_contact)
        layout.addWidget(self.search_button)

        # 결과 출력 레이블
        self.result_label = QLabel("", self)
        layout.addWidget(self.result_label)

        # 레이아웃을 윈도우에 설정
        self.setLayout(layout)

    def add_contact(self):
        # 입력된 이름과 전화번호를 딕셔너리에 추가
        name = self.name_input.text()
        phone = self.phone_input.text()
        if name and phone:
            self.contacts[name] = phone
            self.result_label.setText(f"{name}님의 연락처가 추가되었습니다.")
        else:
            self.result_label.setText("이름과 전화번호를 모두 입력하세요.")
        self.name_input.clear()
        self.phone_input.clear()

    def search_contact(self):
        # 입력된 이름으로 연락처 찾기
        name = self.search_input.text()
        if name in self.contacts:
            self.result_label.setText(f"{name}님의 전화번호: {self.contacts[name]}")
        else:
            self.result_label.setText(f"{name}님의 연락처가 없습니다.")
        self.search_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AddressBookApp()
    window.show()
    sys.exit(app.exec_())
