



def menu():
        menustr = ("""
import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as mb
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog

from tkinter import Button, Frame, Entry, END

from tkinter.scrolledtext import ScrolledText 

import sys
import os



class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent= parent
        self.textwidget = ScrolledText(self.parent, height=50, width=100, bg='white',bd=10)
        self.textwidget.grid(row=10, column=0)
        self.menubar = tk.Menu(self.parent, tearoff=False)
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.view_menu = tk.Menu(self.menubar)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", underline=1, command=lambda : self.clear())
        self.file_menu.add_command(label="Open", underline=1, command=lambda: self.open_file())
        self.file_menu.add_command(label="Save", underline=1, command=lambda:self.save_file())
        self.file_menu.add_command(label="readlines", underline=1, command=lambda : self.readlines())
        self.file_menu.add_command(label="-----", underline=1, command=self.quit)
        self.file_menu.add_command(label="-------", underline=1, command=self.quit)
        self.file_menu.add_command(label="Exit", underline=1, command=self.quit)
        
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", compound="left", underline=0,  command=lambda: self.textwidget.event_generate('<<Copy>>'))
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda: self.undo())
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=lambda : self.redo())
        self.edit_menu.add_command(label="Find", accelerator="Ctrl+F", compound="left", underline=0, command=lambda :self.find())
        self.edit_menu.add_command(label="Replace", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.replace())
        self.edit_menu.add_command(label="cleartags", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.cleartags())
        self.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Backgrounbd Color", compound="left", underline=0,  command=lambda: self.change_bg())
        self.view_menu.add_command(label="Foreground Color",compound="left", underline=0, command=lambda: self.change_fg())
        
    def cleartags(self):
        self.textwidget.tag_config('found', foreground ='black', background = 'white')

    def undo(self):
        try:
            
            self.textwidget.edit_undo()
        except:
            print("No previous action")
    def redo(self):
        try:
            self.textwidget.edit_redo()
        except:
            print("No previous action")




    def copy(self, event=None):
        self.clipboard_clear()
        text = self.textwidget.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)



    def quit(self):
        sys.exit(0)


    def clear(self):

        self.textwidget.delete("1.0", tk.END)
    def cleare1(self):
        self.e1.delete(0, END)
   

    def change_bg(self):
       
        (triple, hexstr) = askcolor()
        if hexstr:
            self.textwidget.config(bg=hexstr)


    def change_fg(self):
       
        (triple, hexstr) = askcolor()
        
        if hexstr:
            self.textwidget.config(fg=hexstr)


    def command(self):
        pass


    def open_file(self):
       
        '''Open a file for editing.'''
        filepath = askopenfilename(filetypes=[("Python Scripts", "*.py"),("Text Files", "*.txt"),('All Files', '*.*')])
        if not filepath:
            return
        self.textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            self.textwidget.insert(tk.END, text)
       
    def save_file(self):
       
        filepath = asksaveasfilename(
            defaultextension='py',
            filetypes=[('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.textwidget.get(1.0, tk.END)
            output_file.write(text)

    def readlines(self):
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*")]
        )
        if not filepath:
            return
        self.textwidget.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.readlines()
            self.textwidget.insert(tk.END, text)
            return filepath2


    def ggtxt(self, textwidget):
        gettxt = self.tx.get("1.0", tk.END)
        self.textwidget.insert(tk.END, gettxt)

   


       
    def edit2(self, name):
        runpy.run_path(path_name="name")
    def find(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
       
        def finder():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
            entry = entry1.get()
      
         
            if (entry1):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(entry, idx, nocase = 1,
                                    stopindex = END)
                     
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(entry))
                     
         
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
             
                self.textwidget.tag_config('found',background="purple", foreground ='yellow')
              
        self.find_btn = tk.Button(top, text="Find", bd=8,command=finder)
        self.find_btn.grid(row=8, column=1)
        entry1.focus_set() 
    

    def replace(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
        label2 = tk.Label(top, text = "Replace With ").grid(row=3, column=1)
        entry2 = tk.Entry(top, width=15, bd=12, bg = "seashell")
        entry2.grid(row=5, column=1)
        def replacer():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
             
            # returns to widget currently in focus
            self.fin = entry1.get()
            self.repl = entry2.get()
             
            if (self.fin and self.repl):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(self.fin, idx, nocase = 1,
                                    stopindex = END)
                    print(idx)
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(self.fin))
         
                    self.textwidget.delete(idx, lastidx)
                    self.textwidget.insert(idx, self.repl)
         
                    lastidx = '% s+% dc' % (idx, len(self.repl))
                     
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
            self.textwidget.tag_config('found', foreground ='green', background = 'yellow')
        self.replace_btn = tk.Button(top, text="Find & Replace", bd=8,command=replacer)
        self.replace_btn.grid(row=8, column=1)
        entry1.focus_set()            
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    app=App()
    app.mainloop()


""")
        self.txt.insert("1.0", menustr)



def notebook():
        notestr = ("""

#!/usr/bin/env python3
import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
import os, sys, subprocess

import pyautogui as pag
import pyperclip as pc
import runpy
import glob
import time


from tkinter.scrolledtext import ScrolledText 

##from NB1 import *
##from NB2 import *
##from NB3 import *
##from frwidget import *
##from codestrings import *

class Note(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
       
        self.notebook.add(self.f1, text="TAB1")
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='2')
                       
                      #################################################################Frame 3################################################################
        self.f3 = ttk.Frame(self.notebook)
        self.notebook.add(self.f3, text='3')
     
        #################################################################################################################################################

        self.f4 = ttk.Frame(self.notebook)
        self.notebook.add(self.f4, text='4')
     

              ########################################################################################
        self.f5 = ttk.Frame(self.notebook)
        self.notebook.add(self.f5, text='5')
       


        ########################################################################################





        f6 = ttk.Frame(self.notebook)
        self.notebook.add(f6, text='6')
      


        ########################################################################################





        f7 = ttk.Frame(self.notebook)
        self.notebook.add(f7, text='7')
        


        ########################################################################################



        f8 = ttk.Frame(self.notebook)
        self.notebook.add(f8, text='8')
        

  


        ########################################################################################
        f9 = ttk.Frame(self.notebook)
        self.notebook.add(f9, text='9')
      
    
            
        ########################################################################################




        f10 = ttk.Frame(self.notebook)
        self.notebook.add(f10, text='10')
    
        ########################################################################################
        f11 = ttk.Frame(self.notebook)
        self.notebook.add(f11, text='11')
        
       


        ########################################################################################


        f12 = ttk.Frame(self.notebook)
        self.notebook.add(f12, text='12')
        
      


        ########################################################################################

        f13 = ttk.Frame(self.notebook)
        self.notebook.add(f13, text='13')
       
        

        f14 = ttk.Frame(self.notebook)
        self.notebook.add(f14, text='14')
        

        f15 = ttk.Frame(self.notebook)
        self.notebook.add(f15, text='15')
       
      

         

        f16 = ttk.Frame(self.notebook)
        self.notebook.add(f16, text='16')
        self.txt16 = ScrolledText(f16, height=1212, width=120)


        f17 = ttk.Frame(self.notebook)
        self.notebook.add(f17, text='17')
      

      


        

        f18 = ttk.Frame(self.notebook)
        self.notebook.add(f18, text='18')
        


        f19 = ttk.Frame(self.notebook)
        self.notebook.add(f19, text='19')
        

      

        f20 = ttk.Frame(self.notebook)
        self.notebook.add(f20, text='20')
       
        
        f21 = ttk.Frame(self.notebook)
        self.notebook.add(f21, text='201')
       

        f22 = ttk.Frame(self.notebook)
        self.notebook.add(f22, text='212')
      

        f23 = ttk.Frame(self.notebook)
        self.notebook.add(f23, text='220')
       
        f24 = ttk.Frame(self.notebook)
        self.notebook.add(f24, text='240')


      
def main():
    parent = tk.Tk()
    app=Note(parent)
    parent.mainloop()


if __name__== '__main__':
    main()

""")
        selk.txt.insert("1.0", notestr)






def chkbtn10():
         chkstr =("""
        self.chk1 = IntVar()
        self.chk2 = IntVar()
        self.chk3 = IntVar()
        self.chk4 = IntVar()
        self.chk5 = IntVar()
        self.chk6 = IntVar()
        self.chk7 = IntVar()
        self.chk8 = IntVar()
        self.chk9 = IntVar()
        self.chk10 = IntVar()

        self.chkbtn1 = tk.Checkbutton(
            root, text="   ", variable=self.chk1, onvalue=1, offvalue=0, height=2, width=10
        )

        self.chkbtn2 = Checkbutton(
            root, text="   ", variable=self.chk2, onvalue=1, offvalue=0, height=2, width=10
        )

        self.chkbtn3 = Checkbutton(
            root, text="   ", variable=self.chk3, onvalue=1, offvalue=0, height=2, width=10
        )


        self.chkbtn4 = Checkbutton(
            root, text="   ", variable=self.chk4, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn5 = Checkbutton(
            root, text="   ", variable=self.chk5, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn6 = Checkbutton(
            root, text="   ", variable=self.chk6, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn7 = Checkbutton(
            root, text="   ", variable=self.chk7, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn8 = Checkbutton(
            root, text="   ", variable=self.chk8, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn9 = Checkbutton(
            root, text="   ", variable=self.chk9, onvalue=1, offvalue=0, height=2, width=10
        )
        self.chkbtn10 = Checkbutton(
            root, text="   ", variable=self.chk10, onvalue=1, offvalue=0, height=2, width=10
        )


        w = Label(root, text=" Title 1 ", font="50")
        w.grid(row=0, column=0)

        aa = Label(root, text=" Title 2 ", font="50")
        aa.grid(row=0, column=1)

        bb = Label(root, text=" Title 3", font="50")
        bb.grid(row=0, column=2)

        cc = Label(root, text="Title 4 ", font="50")
        cc.grid(row=0, column=3)


        self.chkbtn1.grid(row=1, column=3)
        self.chkbtn2.grid(row=2, column=3)
        self.chkbtn3.grid(row=3, column=3)

        self.chkbtn4.grid(row=4, column=3)
        self.chkbtn5.grid(row=5, column=3)
        self.chkbtn6.grid(row=6, column=3)
        self.chkbtn7.grid(row=7, column=3)
        self.chkbtn8.grid(row=8, column=3)
        self.chkbtn9.grid(row=9, column=3)
        self.chkbtn10.grid(row=10, column=3)""")
         self.txt.insert(tk.END, chkstr)                   












