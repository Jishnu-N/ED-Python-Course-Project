#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from PyQt5.QtWidgets import QGridLayout, QGroupBox, QLabel, QSlider, QPushButton, QHBoxLayout, QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Figurecanvas


#Creating a new canvas
class Window(QWidget):
    def __init__(self):
        super().__init__()

    #Initilaistaion dimensions and relevant titles
    def init_ui(self):
        #visual box for the buttons and the graph
        grid_box = QGridLayout()
        grid_box.addWidget(self.create_grp_coeff())
        self.canvas = Figurecanvas(plt.Figure(figsize = (12,6)))
        grid_box.addWidget(self.canvas)
        self.insert_plot()
        
        self.setLayout(grid_box)
        self.setWindowTitle("Parabolas")
        self.show()

        #Defining all the sliders and their properties such as selection range, appearence etc
    def sldr_1(self):
        #slider 1 to change value of coefficient os x^2, 'a'
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(-50)
        self.s1.setMaximum(50)
        self.s1.setValue(0)
        self.s1.setTickInterval(2)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.valueChanged.connect(self.update_label_1)

        self.label1 = QLabel('0', self)
        self.label1.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label1.setMinimumWidth(80)

        self.s1.valueChanged.connect(self.update_plot)

        grp_box_1 =QGroupBox("&Coefficient of x^2 (a)")
        grp_box_1.setAlignment(Qt.AlignHCenter)
        h_box_1 = QVBoxLayout()
        h_box_1.addWidget(self.s1)

        grp_label_1 = QGroupBox()
        H_box_label_1 = QVBoxLayout()
        H_box_label_1.addWidget(self.label1)

        grp_label_1.setLayout(H_box_label_1)
        grp_box_1.setLayout(h_box_1)
        h_box_1.addWidget(grp_label_1)
        return grp_box_1


    def sldr_2(self):
        #slider 2 to decide value of coefficient of x, 'b'
        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(-30)
        self.s2.setMaximum(30)
        self.s2.setValue(0)
        self.s2.setTickInterval(2)
        self.s2.setTickPosition(QSlider.TicksBelow)
        self.s2.valueChanged.connect(self.update_label_2)

        self.label2 = QLabel('0', self)
        self.label2.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label2.setMinimumWidth(80)

        self.s2.valueChanged.connect(self.update_plot)

        grp_box_2 = QGroupBox("&Coefficient of x (b)")
        grp_box_2.setAlignment(Qt.AlignHCenter)
        h_box_2 = QVBoxLayout()
        h_box_2.addWidget(self.s2)

        grp_label_2 = QGroupBox()
        H_box_label_2 = QVBoxLayout()
        H_box_label_2.addWidget(self.label2)

        grp_label_2.setLayout(H_box_label_2)
        grp_box_2.setLayout(h_box_2)
        h_box_2.addWidget(grp_label_2)
        return grp_box_2

    def sldr_3(self):
        #Slider 3 to vary the value of the constant 'c'
        self.s3 = QSlider(Qt.Horizontal)
        self.s3.setMinimum(-50)
        self.s3.setMaximum(50)
        self.s3.setValue(0)
        self.s3.setTickInterval(2)
        self.s3.setTickPosition(QSlider.TicksBelow)
        self.s3.valueChanged.connect(self.update_label_3)

        self.label3 = QLabel('0', self)
        self.label3.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label3.setMinimumWidth(80)

        self.s3.valueChanged.connect(self.update_plot)

        grp_box_3 = QGroupBox("&Constant (c)")
        grp_box_3.setAlignment(Qt.AlignHCenter)
        h_box_3 = QVBoxLayout()
        h_box_3.addWidget(self.s3)

        grp_label_3 = QGroupBox()
        H_box_label_3 = QVBoxLayout()
        H_box_label_3.addWidget(self.label3)

        grp_label_3.setLayout(H_box_label_3)
        grp_box_3.setLayout(h_box_3)
        h_box_3.addWidget(grp_label_3)
        return grp_box_3

    def sldr_4(self):
        #Slider 4
        self.s4 = QSlider(Qt.Horizontal)
        self.s4.setMinimum(-20)
        self.s4.setMaximum(20)
        self.s4.setValue(0)
        self.s4.setTickInterval(2)
        self.s4.setTickPosition(QSlider.TicksBelow)
        self.s4.valueChanged.connect(self.update_label_4)

        self.label4 = QLabel('0', self)
        self.label4.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label4.setMinimumWidth(80)

        self.s4.valueChanged.connect(self.update_plot)

        grp_box_4 = QGroupBox('&Tangent at X')
        grp_box_4.setAlignment(Qt.AlignHCenter)
        h_box_4 = QVBoxLayout()
        h_box_4.addWidget(self.s4)

        grp_label_4 = QGroupBox()
        H_box_label_4 = QVBoxLayout()
        H_box_label_4.addWidget(self.label4)

        grp_label_4.setLayout(H_box_label_4)
        grp_box_4.setLayout(h_box_4)
        h_box_4.addWidget(grp_label_4)
        return grp_box_4
    
   
    #updating values for the text underneath sliders to show its value
    def update_label_1(self, value):
        self.label1.setText(str(value))

    def update_label_2(self, value):
        self.label2.setText(str(value))

    def update_label_3(self, value):
        self.label3.setText(str(value))
    
    # to show equation of tangent at x, as text in the slider text box
    def update_label_4(self, v):
        m=2*self.s1.value()*v + self.s2.value()
        k=self.s1.value()*v**2 + self.s2.value()*v + self.s3.value() - m*v
        out='at x='+ str(v)+', tangent is y='+str(m)+ 'x+' + str(k)
        self.label4.setText(out)


    def create_grp_coeff(self):
        group_box = QGroupBox("&Parameters of the Curve ax^2 + bx + c")
        group_box.setAlignment(Qt.AlignHCenter)
        H_box = QHBoxLayout()
        H_box.setAlignment(Qt.AlignCenter)
        H_box.addWidget(self.sldr_1())
        H_box.addWidget(self.sldr_2())
        H_box.addWidget(self.sldr_3())
        H_box.addWidget(self.sldr_4())
        H_box.addStretch()
        group_box.setLayout(H_box)
        return group_box 

    #Defining the Appearence properties of the graph 
    def insert_plot(self):      
        self.ax = self.canvas.figure.subplots()
        self.ax.set_xlim([-20,20])
        self.ax.set_ylim([-100,100])
        self.ax.grid()
        self.ax.set_title("Parabola")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y(x)")
        self.graph = None

    #function to pass slider input to parabola equation and graph.
    def update_plot(self):
        a = self.s1.value()
        b = self.s2.value()
        x= np.linspace(-19, 19, 4000)
        c = self.s3.value()

        y= a*x**2 + b*x + c        
        
        #Ensuring integer is being passed for easy running and understanding       
        try:
            a = int(a)
        except ValueError:
            a = 0

        try:
            b = int(b)
        except ValueError:
            b = 0

        try:
            c = int(c)
        except ValueError:
            c = 0

        #to remove the drawn graph at every step in order to see only one curve at a time.
        if self.graph:
           self.graph.remove()
     
        #plotting using scatter will be most suitable, 'plot' is suitable for static interface
        self.graph = self.ax.scatter(x,y, s=5)
        self.canvas.draw()
    

#Main function and calling.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    a_window = Window()
    a_window.init_ui()
    sys.exit(app.exec_())

