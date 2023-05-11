

#!/usr/bin/env python3
import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Toplevel, Frame, Scrollbar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory

from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import Tk, Button, BOTH, SUNKEN, END
from tkinter.colorchooser import askcolor
import os, sys, subprocess
from tkinter.scrolledtext import ScrolledText 
import runpy
import glob
import time


from large_snips import *
from tabs345 import *

class Coder(tk.Frame):
    ecount = 1
    btncount = 1
    btncount2 = 1
    labelcount = 1
    canvascount = 1
    lboxcount = 1
    rowcount = 1
    columncount = 1
    combocount = 1
    spincount = 1
    textcount = 1
    slidercount = 1
    scrollcount = 1
    projectcount = 1
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=600, height=600)
        self.f1.grid(row=0, column=1)
        self.notebook.add(self.f1, text="TAB1")
       
        
        self.top = Toplevel()
        self.txt = ScrolledText(self.top, height=50, width=100, bg='white',bd=15)
        self.txt.grid(row=2, column=0,sticky="nsew")
        self.btn1 = tk.Button(self.f1, text="imports", bg="orange", bd=6,command=self.qukimp)
        self.btn1.grid(row=5, column=1)
        self.btn2 = tk.Button(self.f1, text="Entry", bg="orange",bd =6, command=self.e_code)
        self.btn2.grid(row=6, column=1)
        self.btn3 = tk.Button(self.f1, text="Button Code1", bg="orange",bd=6, command=self.button_code)
        self.btn3.grid(row=7, column=1)
        self.btn4 = tk.Button(self.f1, text="Button code2", bg="orange", bd=6,command=self.button_code2)
        self.btn4.grid(row=8, column=1)
        self.btn5 = tk.Button(self.f1, text="Menu OOP", bg="violet",bd =8, command=menu)
        self.btn5.grid(row=9, column=1)
        self.btn6 = tk.Button(self.f1, text="Label1", bg="orange",bd=8, command=self.label_code1)
        self.btn6.grid(row=10, column=1)
        self.btn7 = tk.Button(self.f1, text="Label2", bg="orange",bd=6, command=self.label_code2)
        self.btn7.grid(row=11, column=1)
        self.btn8 = tk.Button(self.f1, text="Notebook empty tabs", bg="orange", bd=6,command=notebook)
        self.btn8.grid(row=12, column=1)
        self.btn9 = tk.Button(self.f1, text="Canvas1", bg="light blue",bd=8, command=self.canvascol)
        self.btn9.grid(row=13, column=1)
        self.btn10 = tk.Button(self.f1, text="Canva2", bg="orange",bd=8, command=self.canvasrow)
        self.btn10.grid(row=14, column=1)
        self.btn11 = tk.Button(self.f1, text="combobox", bg="orange", bd=8, command=self.combo_code)
        self.btn11.grid(row=15, column=1)
        self.btn12 = tk.Button(self.f1, text="combobox2", bg="orange",bd=8, command=self.combo_code2)
        self.btn12.grid(row=16, column=1)
        self.btn13 = tk.Button(self.f1, text="spin box", bg="orange", bd=6,command=self.spin_code)
        self.btn13.grid(row=17, column=1)
        self.btn14 = tk.Button(self.f1, text="spinbox2", bg="orange",bd=6, command=self.spin_code2)
        self.btn14.grid(row=8, column=2)
        self.btn15 = tk.Button(self.f1, text="Text box", bg="light blue",bd=6, command=self.text_code)
        self.btn15.grid(row=7, column=2)
        self.btn16 = tk.Button(self.f1, text="Slider", bg="orange", bd=6,command=self.slider)
        self.btn16.grid(row=6, column=2)
        self.btn17 = tk.Button(self.f1, text="Clear", bg="orange",bd=6, command=self.clear)
        self.btn17.grid(row=5, column=2)
        self.btn18 = tk.Button(self.f1, text="Save", bg="orange",bd=6, command=self.save_code)
        self.btn18.grid(row=22, column=1)
        self.btn19 = tk.Button(self.f1, text="Open", bg="orange", bd=6, command=self.open_code)
        self.btn19.grid(row=23, column=1)
        self.btn20 = tk.Button(self.f1, text="self.", bg="orange", bd=6,command=self.insert_self)
        self.btn20.grid(row=9, column=2)
        self.btn21 = tk.Button(self.f1, text="starter code", bg="orange",bd = 6, command=self.start_code)
        self.btn21.grid(row=10, column=2)
        self.btn23 = tk.Button(self.f1, text="scrolltext", bg="orange",bd=6, command=self.scrolledtxt)
        self.btn23.grid(row=3, column=2)
        self.btn24 = tk.Button(self.f1, text="10 chkbuttons", bg="orange", bd=6,command=chkbtn10)
        self.btn24.grid(row=4, column=2)
##        self.btn25 = tk.Button(self.f1, text="-------", bg="violet",bd =8, command=menu)
##        self.btn25.grid(row=5, column=2)
##        self.btn26 = tk.Button(self.f1, text="----", bg="orange",bd=8, command=self.label_code1)
##        self.btn26.grid(row=6, column=2)
##        self.btn27 = tk.Button(self.f1, text="-----", bg="orange",bd=6, command=self.label_code2)
##        self.btn27.grid(row=7, column=2)
##        self.btn28 = tk.Button(self.f1, text="--------", bg="orange", bd=6,command=notebook)
##        self.btn28.grid(row=8, column=2)
##        self.btn29 = tk.Button(self.f1, text="----", bg="light blue",bd=8, command=self.canvascol)
##        self.btn29.grid(row=9, column=2)
##        self.btn30 = tk.Button(self.f1, text="-------", bg="orange",bd=8, command=self.canvasrow)
##        self.btn30.grid(row=10, column=2)
##        self.btn31 = tk.Button(self.f1, text="------", bg="orange", bd=8, command=self.combo_code)
##        self.btn31.grid(row=11, column=2)
##        self.btn32 = tk.Button(self.f1, text="-------", bg="orange",bd=8, command=self.combo_code2)
##        self.btn32.grid(row=10, column=3)
##        self.btn33 = tk.Button(self.f1, text="--------", bg="orange", bd=6,command=self.spin_code)
##        self.btn33.grid(row=11, column=3)
##        self.btn34 = tk.Button(self.f1, text="-------", bg="orange",bd=6, command=self.spin_code2)
##        self.btn34.grid(row=12, column=3)
##        self.btn35 = tk.Button(self.f1, text="-----", bg="light blue",bd=6, command=self.text_code)
##        self.btn35.grid(row=13, column=3)
##        self.btn36 = tk.Button(self.f1, text="slider", bg="orange", bd=6,command=self.slider)
##        self.btn36.grid(row=14, column=3)
##        self.btn37 = tk.Button(self.f1, text="clear", bg="orange",bd=7, command=self.clear)
##        self.btn37.grid(row=15, column=3)
##        self.btn38 = tk.Button(self.f1, text="save", bg="orange",bd=7, command=self.save_code)
##        self.btn38.grid(row=16, column=3)
##        self.btn39 = tk.Button(self.f1, text="open", bg="orange", bd=6, command=self.open_code)
##        self.btn39.grid(row=17, column=3)
        self.f2 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f2.grid(row=0, column=1)
        self.notebook.add(self.f2, text="TAB2")
##        self.but1 = tk.Button(self.f2, text="imports", bg="orange", bd=6,command=self.qukimp)
##        self.but1.grid(row=5, column=1)
##        self.but2 = tk.Button(self.f2, text="Entry", bg="orange",bd =6, command=self.e_code)
##        self.but2.grid(row=6, column=1)
##        self.but3 = tk.Button(self.f2, text="Button Code1", bg="orange",bd=6, command=self.button_code)
##        self.but3.grid(row=7, column=1)
##        self.but4 = tk.Button(self.f2, text="Button code2", bg="orange", bd=6,command=self.button_code2)
##        self.but4.grid(row=8, column=1)
##        self.but5 = tk.Button(self.f2, text="Menu OOP", bg="violet",bd =8, command=self.menu)
##        self.but5.grid(row=9, column=1)
##        self.but6 = tk.Button(self.f2, text="Label1", bg="orange",bd=8, command=self.label_code1)
##        self.but6.grid(row=10, column=1)
##        self.but7 = tk.Button(self.f2, text="Label2", bg="orange",bd=6, command=self.label_code2)
##        self.but7.grid(row=11, column=1)
##        self.but8 = tk.Button(self.f2, text="Notebook empty tabs", bg="orange", bd=6,command=self.notebook)
##        self.but8.grid(row=12, column=1)
##        self.but9 = tk.Button(self.f2, text="Canvas1", bg="light blue",bd=8, command=self.canvascol)
##        self.but9.grid(row=13, column=1)
##        self.but10 = tk.Button(self.f2, text="Canva2", bg="orange",bd=8, command=self.canvasrow)
##        self.but10.grid(row=14, column=1)
##        self.but11 = tk.Button(self.f2, text="combobox", bg="orange", bd=8, command=self.combo_code)
##        self.but11.grid(row=15, column=1)
##        self.but12 = tk.Button(self.f2, text="combobox2", bg="orange",bd=8, command=self.combo_code2)
##        self.but12.grid(row=16, column=1)
##        self.but13 = tk.Button(self.f2, text="spin box", bg="orange", bd=6,command=self.spin_code)
##        self.but13.grid(row=17, column=1)
##        self.but14 = tk.Button(self.f2, text="spinbox2", bg="orange",bd=6, command=self.spin_code2)
##        self.but14.grid(row=18, column=1)
##        self.but15 = tk.Button(self.f2, text="Text box", bg="light blue",bd=6, command=self.text_code)
##        self.but15.grid(row=19, column=1)
##        self.but16 = tk.Button(self.f2, text="Slider", bg="orange", bd=6,command=self.slider)
##        self.but16.grid(row=20, column=1)
##        self.but17 = tk.Button(self.f2, text="Clear", bg="orange",bd=6, command=self.clear)
##        self.but17.grid(row=21, column=1)
##        self.but18 = tk.Button(self.f2, text="Save", bg="orange",bd=6, command=self.save_code)
##        self.but18.grid(row=22, column=1)
##        self.but19 = tk.Button(self.f2, text="Open", bg="orange", bd=6, command=self.open_code)
##        self.but19.grid(row=23, column=1)
##        self.but20 = tk.Button(self.f2, text="self.", bg="orange", bd=6,command=self.insert_self)
##        self.but20.grid(row=0, column=1)
##        self.but21 = tk.Button(self.f2, text="starter code", bg="orange",bd = 6, command=self.start_code)
##        self.but21.grid(row=0, column=2)
##        self.but23 = tk.Button(self.f2, text="scrolltext", bg="orange",bd=6, command=self.scrolledtxt)
##        self.but23.grid(row=3, column=2)
##        self.but24 = tk.Button(self.f2, text="10 chkbuttons", bg="orange", bd=6,command=self.chkbut10)
##        self.but24.grid(row=4, column=2)
##        self.but25 = tk.Button(self.f2, text="-------", bg="violet",bd =8, command=self.menu)
##        self.but25.grid(row=5, column=2)
##        self.but26 = tk.Button(self.f2, text="----", bg="orange",bd=8, command=self.label_code1)
##        self.but26.grid(row=6, column=2)
##        self.but27 = tk.Button(self.f2, text="-----", bg="orange",bd=6, command=self.label_code2)
##        self.but27.grid(row=7, column=2)
##        self.but28 = tk.Button(self.f2, text="--------", bg="orange", bd=6,command=self.notebook)
##        self.but28.grid(row=8, column=2)
##        self.but29 = tk.Button(self.f2, text="----", bg="light blue",bd=8, command=self.canvascol)
##        self.but29.grid(row=9, column=2)
##        self.but30 = tk.Button(self.f2, text="-------", bg="orange",bd=8, command=self.canvasrow)
##        self.but30.grid(row=10, column=2)
##        self.but31 = tk.Button(self.f2, text="------", bg="orange", bd=8, command=self.combo_code)
##        self.but31.grid(row=11, column=2)
##        self.but32 = tk.Button(self.f2, text="-------", bg="orange",bd=8, command=self.combo_code2)
##        self.but32.grid(row=10, column=3)
##        self.but33 = tk.Button(self.f2, text="--------", bg="orange", bd=6,command=self.spin_code)
##        self.but33.grid(row=11, column=3)
##        self.but34 = tk.Button(self.f2, text="-------", bg="orange",bd=6, command=self.spin_code2)
##        self.but34.grid(row=12, column=3)
##        self.but35 = tk.Button(self.f2, text="-----", bg="light blue",bd=6, command=self.text_code)
##        self.but35.grid(row=13, column=3)
##        self.but36 = tk.Button(self.f2, text="slider", bg="orange", bd=6,command=self.slider)
##        self.but36.grid(row=14, column=3)
##        self.but37 = tk.Button(self.f2, text="clear", bg="orange",bd=7, command=self.clear)
##        self.but37.grid(row=15, column=3)
##        self.but38 = tk.Button(self.f2, text="save", bg="orange",bd=7, command=self.save_code)
##        self.but38.grid(row=16, column=3)
##        self.but39 = tk.Button(self.f2, text="open", bg="orange", bd=6, command=self.open_code)
##        self.but39.grid(row=17, column=3)
        self.f3 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f3.grid(row=0, column=2)
        self.notebook.add(self.f3, text="view")
        self.view = Codeview(self.f3)
        













        self.f4 = ttk.Frame(self.notebook, width=600, height=600)
        self.f4.grid(row=0, column=1)
        self.notebook.add(self.f4, text="TAB4")
       

    def start_code(self):
        starter = ("""
import tkinter
from tkinter import *




class Something(object):
    def __init__(self, *args, *kwargs):
        self.var1 = 0
        self.var2 = 0
        self.var3 = None
        self.var4 = 0
        self.method1()
    def method1(self):
        """)
        self.txt.insert(tk.END, starter)


        
    def insert_self(self):
        self.str = ("""
        self.""")
        self.txt.insert(tk.END, self.str)

    def qukimp(self):
        qpo = (
        """

import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame
from tkinter import *
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time"""
            + "\n"
        )
        self.txt.insert(tk.END, qpo)


    def e_code(self):
      
        w_str = (
            """    self.var = tk.StringVar(self)
    self.e1 = tk.Entry(self, self.textvariable=self.var, bg='snow')
    self.e1.grid(row=3, column=4)"""
            + "\n"
        )
        w_str2 = w_str.replace("self.var1", "self.var" + str(self.ecount))
        w_str3 = w_str2.replace("self.e1", "self.e" + str(self.ecount))
        w_str4 = w_str3.replace("row=3", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, w_str4)
        self.ecount += 1
        self.rowcount += 1

    def button_code(self):
       
        w_str = (
            """
    self.b1 = tk.Button(root,relief=tk.FLAT, compound=tk.LEFT,text="new",command=None)
    self.b1.grid(row=1, column=2)"""
            + "\n"
        )
        w_str2 = w_str.replace("b1", "b" + str(self.btncount))
        w_str3 = w_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, w_str3)
        self.btncount += 1
        self.rowcount += 1

    def button_code2(self):
    
        w_str = (
            """    self.btn1 = tk.Button(self,
                    relief=tk.FLAT,
                    compound=tk.LEFT,
                    self.text="new",
                    command=None,

                )
    self.btn1.grid(row=2, column=1)"""
            + "\n"
        )
        w_str2 = w_str.replace("self.btn1", "self.btn" + str(self.btncount2))
        w_str3 = w_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, w_str3)
        self.btncount2 += 1
        self.columncount += 1





    def label_code1(self):
       
        label_str = (
            """self.label1 = tk.Label(self,
            self.ft = tkFont.Font(family='Ariel Black',size=10)
            self.label1["font"] = ft
            self.label1["fg"] = "#333333",
            self.label1["justify"] = "center",
            self.label1["text"] = "label",
            width=100,height=25)
self.label1.grid(row=4, column=2)"""
            + "\n"
        )
        label_str2 = label_str.replace("self.label1", "self.label" + str(self.labelcount))
        label_str3 = label_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, label_str3)
        self.labelcount += 1
        self.rowcount += 1

    def label_code2(self):
    
        label_str = (
            """self.label1 = tk.Label(self,
            self.ft = tkFont.Font(family='Ariel Black',size=10)
            self.label1["font"] = ft
            self.label1["fg"] = "#333333",
            self.label1["justify"] = "center",
            self.label1["text"] = "label",
            width=100,height=25)
self.label1.grid(row=5, column=2)"""
            + "\n"
        )
        label_str2 = label_str.replace("self.label1", "self.label" + str(self.labelcount))
        label_str3 = label_str2.replace("column=1", "column=" + str(self.columncount))
        text.insert(tk.END, label_str3)
        self.labelcount += 1
        self.columncount += 1



    def canvascol(self):

        canvas_str = (
                    """
        self.canvas1 = tk.Canvas(self, height=300, width=800, background="cornsilk")
        #self.canvas1.configure( )
        self.canvas1.grid(row=1, column=1)
        #self.canvas1.create_line(x1, y1, x2, y2, fill="black" width=1)"""
                    + "\n"
        )

        canvas_str2 = canvas_str.replace("self.canvas1", "self.canvas" + str(self.canvascount))

        canvas_str3 = canvas_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert("1.0", canvas_str3)
        self.canvascount += 1
        self.columncount += 1

    def canvasrow(self):
      

        canvas_str = (
                """
    self.canvas1 = tk.Canvas(self, height=300, width=800, background="cornsilk")
    self.canvase grid(row=1, column=1)"""
            + "\n"
        )

        canvas_str2 = canvas_str.replace("self.canvas1", "self.canvas" + str(self.canvascount))
        
        canvas_str4 = canvas_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert("1.0", canvas_str4)
        self.canvascount += 1
        self.rowcount += 1

    def combo_code(self):
    
        combo_str = (
            """
    self.cb1 = ttk.Combobox(self, values=["Value1", "value2, "value3"])
    self.cb1.grid(column=0, row=1)"""
            + "\n"
        )
        combo_str2 = combo_str.replace("self.cb1", "self.cb" + str(self.combocount))
        combo_str3 = combo_str2.replace("row=1", "row=" + str(rowcount))
        self.txt.insert(tk.END, combo_str3)
        self.combocount += 1
        self.rowcount += 1

    def combo_code2(self):
    
        combo_str = (
                """
    self.cb1 = ttk.Combobox(self, values=["Value1", "value2, "value3"])
    self.cb1.grid(column=1, row=1)"""
            + "\n"
        )
        combo_str2 = combo_str.replace("self.cb1", "self.cb" + str(self.combocount))
        combo_str3 = combo_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, combo_str3)
        self.combocount += 1
        self.columncount += 1

    def spin_code(self):
       
        spin_str = (
            """
    self.sp1 = tk.Spinbox(self, from_=1.0, to=1000.0, increment=0.1)
    self.sp1.grid(row=1, column=0)"""
            + "\n"
        )
        spin_str2 = spin_str.replace("self.sp1", "self.sp" + str(self.spincount))
        spin_str3 = spin_str2.replace("row=1", "row=" + str(self.rowcount))
        self.txt.insert(tk.END, spin_str3)
        self.spincount += 1
        self.rowcount += 1

    def spin_code2(self):
      
        spin_str = (
            """
    self.sp1 = tk.Spinbox(self, from_=1.0, to=1000.0, increment=0.1)
    self.sp1.grid(row=1, column=0)"""
            + "\n"
        )
        spin_str2 = spin_str.replace("self.sp1", "self.sp" + str(self.spincount))
        spin_str3 = spin_str2.replace("column=1", "column=" + str(self.columncount))
        self.txt.insert(tk.END, spin_str3)
        self.spincount += 1
        self.columncount += 1

    def text_code(self):
       
        txt_str = (
            """
        self.txt1 = tk.Text(self, height=60, width=150, bg='white')
        self.txt1.insert('1.0', tk.END)
        self.txt1.grid(row=2, column=3)"""
            + "\n"
        )
        txt_str2 = txt_str.replace("txt1", "txt" + str(self.textcount))
        self.txt.insert(tk.END, txt_str2)
        self.textcount += 1

    def slider(self):
        sld_str = ("""
        self.slider1 = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='vertical',  # horizontal

        """ + "\n")
        slider_str2 = slidar_str.replace("self.slider1", "self.slider" + str(self.slidercount))
        self.txt.insert(tk.END, slider_str2)
        self.slidercount += 1
        self.txt.insert(tk.END, sld_str)

    def scrolledtxt(self):

        importstr = ("\n"+ """ 
from tkinter import scrolledtext as st""" + "\n")
        txtstr = ("""

    class Txt_Widget:(object):
        def __init__(self, parent):
            self.parent = parent
            self.txt = st.ScrolledText(self.top, height=50, width=100, bg='white',bd=15)
            self.txt.grid(row=2, column=0, sticky="nsew") """ )

        self.txt.insert("3.0", importstr)         
        self.txt.insert(tk.END, txtstr)






    def clear(self):
        self.txt.delete("1.0", tk.END)

    def open_code(self):
        # file type
        filetypes = [
            ("Python files", "*.py"),
            ("text files", "*.txt"),
            ("All files", "*.*"),
        ]
        # show the open file dialog
        f = filedialog.askopenfile(filetypes=filetypes)
        # read the text file and show its content on the Text
        self.txt.insert("1.0", f.read)




    def save_code(self):
        stop_str = ("""
if __name__== '__main__':
    app = App()
    app.mainloop()""")
        self.txt.insert(tk.END, stop_str)

     
        filepath = asksaveasfilename(
            defaultextension='.py',
            filetypes=[("Python", "*.py"), ("All Files", "*.*")])
        
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.txt.get(1.0, tk.END)
            output_file.write(text)









class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Coder(self)
        self.geometry('1200x1000')
        self.resizable(True, True)

if __name__ == "__main__":
    app=App()
    app.mainloop()

