from PyQt5 import QtWidgets, uic
import re

def is_valid_text(text):
    pattern = r"^(?:\d+(?:\.\d+)?(?:[-+%/*]\d+(?:\.\d+)?)*(?:[-+%/*])?)$"
    match= re.match(pattern,text)
    if match:
        return True
    else:
        return False
def Change_to_machine_form(text):
    text = text.replace("÷", "/")
    text = text.replace("×", "*")
    return text
def calculate(text):

    operations = []
    final_answer = 0
    for i in range(len(text)):
        if text[i] in ['*', '/','%']:
            operations.append(text[i])
    for i in range(len(text)):
        if text[i] in ['-', '+']:
            operations.append(text[i])
    list_text = []
    list_text += text
    while True:
        for i in range(len(list_text)):
            final_answer = 0
            str_number1 = ""
            str_number2 = ""
            if list_text[i] == operations[0]:
                k = i-1
                while  k!=-1 and list_text[k] not in ['-', '+' ,'*', '/','%' , 'k']:
                    k-=1
                    if list_text[k] in ['-', '+' ,'*', '/','%'] or k==-1:
                        k+=1
                        while list_text[k] not in ['-', '+' ,'*', '/','%' , 'k']:
                            str_number1 += list_text[k]
                            list_text[k] = 'k'
                            k+=1
                k = i+1
                while k!=len(list_text) and list_text[k] not in ['-', '+' ,'*', '/','%' , 'k']:
                    str_number2 +=list_text[k]
                    list_text[k]='k'
                    k+=1
                if str_number1 =="":
                    str_number1=0
                if str_number2 =="":
                    str_number2=0
                if operations[0] =='*':
                    final_answer += float(str_number1) * float(str_number2)
                if operations[0] =='+':
                    final_answer += float(str_number1) + float(str_number2)
                if operations[0] =='-':
                    final_answer += float(str_number1) - float(str_number2)
                if operations[0] =='/':
                    final_answer += float(str_number1) / float(str_number2)
                if operations[0] =='%':
                    final_answer += float(str_number1) % float(str_number2)
                list_text = [item for item in list_text if 'k' not in item]
                list_text = list(map(lambda x: str(final_answer) if x == operations[0] else x, list_text))
                del operations[0]
                break
        if len(operations) == 0:
            break
    return final_answer
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('view.ui', self)
        #Numbers
        self.button0 = self.findChild(QtWidgets.QPushButton, 'pushButton_0') 
        self.button1 = self.findChild(QtWidgets.QPushButton, 'pushButton_1') 
        self.button2 = self.findChild(QtWidgets.QPushButton, 'pushButton_2') 
        self.button3 = self.findChild(QtWidgets.QPushButton, 'pushButton_3') 
        self.button4 = self.findChild(QtWidgets.QPushButton, 'pushButton_4') 
        self.button5 = self.findChild(QtWidgets.QPushButton, 'pushButton_5') 
        self.button6 = self.findChild(QtWidgets.QPushButton, 'pushButton_6') 
        self.button7 = self.findChild(QtWidgets.QPushButton, 'pushButton_7') 
        self.button8 = self.findChild(QtWidgets.QPushButton, 'pushButton_8') 
        self.button9 = self.findChild(QtWidgets.QPushButton, 'pushButton_9') 

        self.button0.clicked.connect(self.pushbutton_0)
        self.button1.clicked.connect(self.pushbutton_1)
        self.button2.clicked.connect(self.pushbutton_2)
        self.button3.clicked.connect(self.pushbutton_3)
        self.button4.clicked.connect(self.pushbutton_4)
        self.button5.clicked.connect(self.pushbutton_5)
        self.button6.clicked.connect(self.pushbutton_6)
        self.button7.clicked.connect(self.pushbutton_7)
        self.button8.clicked.connect(self.pushbutton_8)
        self.button9.clicked.connect(self.pushbutton_9)
        #Functions
        self.button_cross = self.findChild(QtWidgets.QPushButton, 'pushButton_*') 
        self.button_minus = self.findChild(QtWidgets.QPushButton, 'pushButton_-') 
        self.button_plus = self.findChild(QtWidgets.QPushButton, 'pushButton_+') 
        self.button_divide = self.findChild(QtWidgets.QPushButton, 'pushButton_/') 
        self.button_percent = self.findChild(QtWidgets.QPushButton, 'pushButton_%') 

        self.button_cross.clicked.connect(self.pushbutton_cross)
        self.button_minus.clicked.connect(self.pushbutton_minus)
        self.button_plus.clicked.connect(self.pushbutton_plus)
        self.button_divide.clicked.connect(self.pushbutton_divide)
        self.button_percent.clicked.connect(self.pushbutton_percent)

        #Rest
        self.button_C = self.findChild(QtWidgets.QPushButton, 'pushButton_C') 
        self.button_X = self.findChild(QtWidgets.QPushButton, 'pushButton_X') 

        self.button_C.clicked.connect(self.pushbutton_C)
        self.button_X.clicked.connect(self.pushbutton_X)

        self.button_C = self.findChild(QtWidgets.QPushButton, 'pushButton_=') 
        self.button_C.clicked.connect(self.pushbutton_equal)

        if not self.textEdit.toPlainText():
            self.textEdit.setPlainText("0")


        self.textEdit = self.findChild(QtWidgets.QTextEdit, 'textEdit')
        self.textEdit.setReadOnly(True)
        self.show()

    def pushbutton_1(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "1"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_2(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "2"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_3(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "3"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_4(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "4"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_5(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "5"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_6(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "6"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_7(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "7"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_8(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ''
        text += "8"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_9(self):
        text = self.textEdit.toPlainText()
        if text == '0':
            text = ""
        text += "9"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_dot(self):
        text = self.textEdit.toPlainText()
        text += "."
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_cross(self):
        text = self.textEdit.toPlainText()
        if text !="":
            text += "×"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_minus(self):
        text = self.textEdit.toPlainText()
        if text !="":
            text += "-"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_plus(self):
        text = self.textEdit.toPlainText()
        if text !="":
            text += "+"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_percent(self):
        text = self.textEdit.toPlainText()
        if text !="":
            text += "%"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_divide(self):
        text = self.textEdit.toPlainText()
        if text !="":
            text += "÷"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    def pushbutton_0(self):
        text = self.textEdit.toPlainText()
        text += "0"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)

    #Clear
    def pushbutton_X(self):
        text = self.textEdit.toPlainText()
        new_text = ""
        if len(text) == 1:
            new_text = '0'
        else:
            for i in range(len(text)):
                if i !=len(text)-1:
                    new_text+=text[i]
        self.textEdit.setText(new_text)
    #Clear
    def pushbutton_C(self):
        text = self.textEdit.toPlainText()
        text = "0"
        new_text = Change_to_machine_form(text)
        if is_valid_text(new_text):
            self.textEdit.setText(text)
    def pushbutton_equal(self):
        text = self.textEdit.toPlainText()
        text = str(calculate(Change_to_machine_form(text)))
        self.textEdit.setText(text)
app = QtWidgets.QApplication([])
window = Ui()
app.exec_()