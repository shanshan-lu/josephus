#encoding:utf-8
import sys
sys.path.append('../LSS/Josephus problem')
from achieve.achieve import Achieve
from show.UI import Ui_Form
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5.QtCore import QDir
from tkinter import filedialog
import tkinter as tk



class Show(QMainWindow,Ui_Form):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.select_file.clicked.connect(self.open_file)
        self.pushButton.clicked.connect(self.get_text)
        self.start_josephus.clicked.connect(self.run)
           
    def open_file(self):
        '''
        global filename
        filename,fileType = QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), 
        "All Files(*);;Text Files(*.txt);;Xlsx Files(*.xlsx);;Csv Files(*.csv);;Json Files(*.json)")
        self.file_name.setText(filename)
        
        with filename:
            data = Sign.select_resder(filename)
            self.textEdit.setPlainText(data)
        
        f = open(filename,'r')
        with f:
            data = f.read()
            self.textEdit.setText(data)
        '''
        global filepath
        root = tk.Tk()
        root.withdraw()
        filepath =filedialog.askopenfilename()
        self.file_name.setText(filepath)
        
    def get_text(self):
        global start_number,step_number
        start_number = int(self.start_number.text())
        step_number = int(self.step_number.text())        
        
    def run(self):
        sample = Achieve()
        people = sample.select_resder(filepath)
        self.textEdit.setPlainText(str(people))
        sample.create_people()
        sample.set_start(start_number) 
        sample.set_step(step_number)
        sample.set_josephus_sample()
        result = sample.output_outcome()
        self.show_result.setPlainText(str(result))        
    '''
        people = Sign.select_resder(filepath)
        self.textEdit.setPlainText(people)
        Sign.create_people()
        Sign.set_start(self.start_number.text())
        Sign.set_step(self.step_number.text())
        Sign.set_josephus_sample()
        result = Sign.output_outcome()
        self.show_result.setPlainText(result)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Show()
    example.show()
    sys.exit(app.exec_())

