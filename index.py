#project 1 : 15.08.2026
#making a desktop app for Compound Interest calculator

from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QFrame,QTextEdit,QPushButton,QMessageBox
import sys



class fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1000,900)
        self.setFixedSize(1000,1100)
        self.setStyleSheet("background-color:#FFB6C1;")
        self.setWindowTitle("Compound Interest Compound")

        # main title
        self.title=QLabel("Compound Interest Calculator", self)
        self.title.setStyleSheet("color:#800020;font-size:40px ;font-family:Arial;font-weight:bold;")
        self.title.setGeometry(230,-80,600,300)
        
        #frame 1
        self.frame1=QFrame(self)
        self.frame1.setGeometry(170,160,700,780)
        self.frame1.setStyleSheet("background-color:#C084FC;border-radius:20px;")
        #----inputs-------
        self.principal=QLabel("Enter the Principle:", self.frame1)
        self.principal.setGeometry(30,0,300,100)
        self.principal.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:20px;")
        self.principal_input=QTextEdit(self.frame1)
        self.principal_input.setGeometry(30,70,640,55)
        self.principal_input.setPlaceholderText("Principal (DH) ")
        self.principal_input.setStyleSheet("border: 2px solid #C084FC;padding: 10px;border-radius: 8px; background:#FFF8F0;")
        
        self.rate=QLabel("Enter the interest rate %:", self.frame1)
        self.rate.setGeometry(30,130,300,70)
        self.rate.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:20px;")
        self.rate_input=QTextEdit(self.frame1)
        self.rate_input.setGeometry(30,200,640,55)
        self.rate_input.setPlaceholderText("Annual interest rate(%)")
        self.rate_input.setStyleSheet("border: 2px solid #C084FC;padding: 10px;border-radius: 8px; background:#FFF8F0;")
        
        self.years=QLabel("Enter the number of the years:", self.frame1)
        self.years.setGeometry(30,270,300,70)
        self.years.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:20px;")
        self.years_input=QTextEdit(self.frame1)
        self.years_input.setGeometry(30,345,640,55)
        self.years_input.setPlaceholderText("Years")
        self.years_input.setStyleSheet("border: 2px solid #C084FC;padding: 10px;border-radius: 8px; background:#FFF8F0;")
        
        self.times_compound_per_year=QLabel("Enter the number of times compound per year:", self.frame1)
        self.times_compound_per_year.setGeometry(30,410,500,70)
        self.times_compound_per_year.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:20px;")
        self.times_compound_per_year_input=QTextEdit(self.frame1)
        self.times_compound_per_year_input.setGeometry(30,480,640,55)
        self.times_compound_per_year_input.setPlaceholderText("times compound per year")
        self.times_compound_per_year_input.setStyleSheet("border: 2px solid #C084FC;padding: 10px;border-radius: 8px; background:#FFF8F0;")
        
        #buttons
        self.calculate_btn=QPushButton("Calculate" ,self.frame1)
        self.calculate_btn.setGeometry(30,560,270,60)
        self.calculate_btn.setStyleSheet("background: #4C1b5E;color:#FFF8f0;font-weight:bold; font-size:15cv px;padding:10px 20px;border:none;border-radius:8px;")
        self.calculate_btn.clicked.connect(self.calculate)
        
        self.refresh_btn=QPushButton("Refresh" ,self.frame1)
        self.refresh_btn.setGeometry(401,560,270,60)
        self.refresh_btn.setStyleSheet("background: #4C1b5E;color:#FFF8f0;font-weight:bold; font-size:15cv px;padding:10px 20px;border:none;border-radius:8px;")
        self.refresh_btn.clicked.connect(self.refresh)
        
        self.exit_btn=QPushButton("Exit" ,self.frame1)
        self.exit_btn.setGeometry(30,640,640,60)
        self.exit_btn.setStyleSheet("background: #4C1b5E;color:#FFF8f0;font-weight:bold; font-size:15cv px;padding:10px 20px;border:none;border-radius:8px;")
        self.exit_btn.clicked.connect(self.close)
        
        #self.frame1.hide()
        
        #---------------------frame 2 result:---------
        self.frame2=QFrame(self)
        self.frame2.setGeometry(170,160,700,350)
        self.frame2.setStyleSheet("background-color:#C084FC;border-radius:20px;")
        
        self.result1=QLabel("Result:", self.frame2)
        self.result1.setGeometry(30,0,300,100)
        self.result1.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:50px;")

        self.result=QLabel("", self.frame2)
        self.result.setGeometry(30,100,500,100)
        self.result.setStyleSheet("color:#4C1B5E;font-family:arial;font-weight:bold;font-size:20px;")
        
        self.refresh1_btn=QPushButton("Refresh" ,self.frame2)
        self.refresh1_btn.setGeometry(30,250,270,60)
        self.refresh1_btn.setStyleSheet("background: #4C1b5E;color:#FFF8f0;font-weight:bold; font-size:15cv px;padding:10px 20px;border:none;border-radius:8px;")
        self.refresh1_btn.clicked.connect(self.refresh)
        
        self.exit1_btn=QPushButton("Exit" ,self.frame2)
        self.exit1_btn.setGeometry(401,250,270,60)
        self.exit1_btn.setStyleSheet("background: #4C1b5E;color:#FFF8f0;font-weight:bold; font-size:15cv px;padding:10px 20px;border:none;border-radius:8px;")
        self.exit1_btn.clicked.connect(self.close)
        self.frame2.hide()
        
    def calculate(self):
        try:
            p=float(self.principal_input.toPlainText())
            r=float(self.rate_input.toPlainText())
            t=int(self.years_input.toPlainText())
            n=int(self.times_compound_per_year_input.toPlainText())
            
            rate_decimal=r/100
            Amount = p * (1+(rate_decimal/n)) ** (n*t)
            Interest=Amount-p
            self.result.setText(f"After {t} years, the total will be :{Amount:.2f}MAD\nInterest Earned : {Interest:.2f} MAD")
            print(Amount)
            self.frame1.hide()
            self.frame2.show()
        except:
            QMessageBox.warning(self,"Error","Enter valid number")
            self.frame1.show()
            self.frame2.hide()
            self.principal_input.clear()
            self.rate_input.clear()
            self.years_input.clear()
            self.times_compound_per_year_input.clear()
    def refresh(self):
        self.frame1.show()
        self.frame2.hide()
        self.principal_input.clear()
        self.rate_input.clear()
        self.years_input.clear()
        self.times_compound_per_year_input.clear()
    
def main():
    app=QApplication(sys.argv)
    window=fenetre()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()