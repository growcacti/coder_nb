

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



class Codeview(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
        self.notebook.add(self.f1, text="TAB1")
        self.fram = tk.Frame(self.f1, width=100, height=20)
        self.fram.grid(row=0, column=0)
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='2')
        self.textwidget = ScrolledText(self.f2, height=55, width=100)

        self.textwidget.grid(row=0, column=1)
        self.textwidget.grid_rowconfigure(0, weight=1)
        self.textwidget.grid_columnconfigure(1, weight=1)
        self.textwidget.insert("1.0","")

               
        sidebtn = SideButtonframe(self.f2, self.textwidget)

        self.lb = tk.Listbox(self.f1, bg='cyan2',bd=12, width=35, height=55, exportselection=False, selectmode=tk.SINGLE)
        self.lb.grid(row=0, column=2)
        self.lb.focus()
        self.lb.configure(selectmode="")
        
        self.curtxt = None
        self.x = self.lb.curselection()
        self.tx = ScrolledText(self.f1,
                      bg='white',
                      bd=12,
                      relief=GROOVE,
                      height=50,
                      width=100,
                      font='TkFixedFont',)
        self.tx.grid(row = 0, column=5)
        self.cvw = Cview_Buttons(self.f1,self.tx,self.lb, self.textwidget)

        self.flist2 = []
        self.flist = os.listdir(self.path)
        self.lb.insert(tk.END, self.flist)
        for self.item in self.flist:
            if self.item.endswith(".py"):
                self.flist2.append(self.item)

                self.lb.insert(tk.END, self.item)
         
                self.lb.focus()
              
      
       
        self.lb.bind("<Double-Button-1>", self.cvw.listing)
        self.lb.bind("<<ListboxSelect>>", self.cvw.showcontent)
        self.lb.bind("<Double-Button-2>", lambda event: self.cvw.run(self.lb))
        self.lb.bind('<<ListboxSelect>>', lambda event: self.cvw.listing(event))

    



   

   


    

class FindReplaceWidget:
    
    def __init__ (self, parent, textwidget):
        self.fr_buttons = ttk.Frame(parent, relief=tk.RAISED)
        self.label1 = tk.Label(self.fr_buttons, text ='Find').grid(row=11, column=0)
        self.entry = tk.Entry(self.fr_buttons, width=15,bd=12,bg="wheat")
        self.entry.grid(row=12, column=0)

        self.find1 = tk.Button(self.fr_buttons, text ='Find', bd=8)
        self.find1.grid(row=13,column=0)
        self.label2 = tk.Label(self.fr_buttons, text = "Replace With ").grid(row=14, column=0)

        self.entry2 = tk.Entry(self.fr_buttons, width=15,bd=12, bg = "seashell")
        self.entry2.grid(row=15, column=0)
        self.entry2.focus_set()

        self.replace1 = tk.Button(self.fr_buttons, text = 'Find&Replace',bd=8)
        self.replace1.grid(row=16, column=0)


        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.find1.config(command = lambda : self.find(self.textwidget, self.entry2.get()))
        self.replace1.config(command = lambda : self.findNreplace(self.text, self.entry2.get() ,self.entry22.get()))

    def find(self, textwidget,entrywidget):
     
    # remove tag 'found' from index 1 to END
        textwidget.tag_remove('found', '1.0', END)
        self.entry = entrywidget
  
     
        if (self.entry):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.entry, idx, nocase = 1,
                                stopindex = END)
                 
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.entry))
                 
     
                # overwrite 'Found' at idx
                textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
 
        # mark located string as red
         
        textwidget.tag_config('found', foreground ='blue')
       


    

    def findNreplace(self,textwidget,entry1,entry2):
         
        # remove tag 'found' from index 1 to END
        textwidget.tag_remove('found', '1.0', END)
         
        # returns to widget currently in focus
        self.fin = entry1
        self.repl = entry2
         
        if (self.fin and self.repl):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = textwidget.search(self.fin, idx, nocase = 1,
                                stopindex = END)
                print(idx)
                if not idx: break
                 
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(self.fin))
     
                textwidget.delete(idx, lastidx)
                textwidget.insert(idx, self.repl)
     
                lastidx = '% s+% dc' % (idx, len(self.repl))
                 
                # overwrite 'Found' at idx
                textwidget.tag_add('found', idx, lastidx)
                idx = lastidx
     
            # mark located string as red
            textwidget.tag_config('found', foreground ='green', background = 'yellow')
            
class SideButtonframe(ttk.Frame):
    def __init__(self, container, textwidget):
        super().__init__(container)
        self.textwidget = textwidget
        self.parent = container
        self.fr_buttons = tk.Frame(self.parent, relief=tk.RAISED)
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.textwidget.grid(row=0, column=1, sticky="nsew")
        
        self.btn_open = tk.Button(self.fr_buttons, text="Open",bd=4, command=lambda: self.open_file(self.textwidget))
        self.btn_open.grid(row=1, column=0, pady=5)
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...", bd=4,command=lambda: self.save_file(self.textwidget))
        self.btn_save.grid(row=2, column=0, pady=5)
        self.btn_clear = tk.Button(self.fr_buttons, text="Clear",bd=4, command=lambda: self.clear(self.textwidget))
        self.btn_clear.grid(row=3, column=0, pady=5)
      
        self.ftcolor2 = tk.Button(self.fr_buttons, text="Change FG Color",bd=4, command=lambda: self.changeFg(self.textwidget))
        self.ftcolor2.grid(row=6, column=0, pady=5)
        self.btcolor2 = tk.Button(self.fr_buttons, text="Change BG Color",bd=4, command=lambda: self.changeBg(self.textwidget))
        self.btcolor2.grid(row=7, column=0, pady=5)
        self.btnall = tk.Button(self.fr_buttons, text="Select All", bd=4, command=lambda: self.textwidget.event_generate("<<SelectAll>>"))
        self.btnall.grid(row=8, column=0, pady=5)
        self.btncut = tk.Button(self.fr_buttons, text="Cut", bd=4, command=lambda: self.textwidget.event_generate("<<Cut>>"))
        self.btncut.grid(row=9, column=0, pady=5)
        self.btncopy = tk.Button(self.fr_buttons, text="Copy", bd=4, command=lambda: self.textwidget.event_generate('<<Copy>>'))
        self.btncopy.grid(row=10, column=0, pady=5)
        self.btnpaste = tk.Button(self.fr_buttons, text="Paste", bd=4, command=lambda: self.textwidget.event_generate("<<Paste>>"))
        self.btnpaste.grid(row=11, column=0, pady=5)
        self.btnundo = tk.Button(self.fr_buttons, text="Undo", bd=4, command=lambda: self.undo())
        self.btnundo.grid(row=12, column=0, pady=5)
        self.btnredo = tk.Button(self.fr_buttons, text="Redo", bd=4, command=lambda: self.redo())
        self.btnredo.grid(row=13, column=0, pady=5)

        self.binding()

    def binding(self):
        self.textwidget.bind
    def changeBg(self,textwidget):
            (triple, hexstr) = askcolor()
            if hexstr:
                textwidget.config(bg=hexstr)


    def changeFg(self,textwidget):
        (triple, hexstr) = askcolor()
        if hexstr:
            textwidget.config(fg=hexstr)


    def clear(self, textwidget):
        self.textwidget = textwidget
        self.textwidget.delete("1.0", tk.END)


    def open_file(self,textwidget):
        '''Open a file for editing.'''
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.self.txt'), ('All Files', '*.*')]
        )
        if not filepath:
            return
        textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            textwidget.insert(tk.END, text)
       
    def save_file(self,textwidget):
        '''Save the current file as a new file.'''
        filepath = asksaveasfilename(
            defaultextension='self.txt',
            filetypes=[('Text Files', '*.self.txt'), ('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = textwidget.get(1.0, tk.END)
            output_file.write(text)




    


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


    def select_all(self, event=None):
        self.textwidget.tag_add("sel", "1.0", tk.END)
        return "break"




    def quit(self):
        sys.exit(0)


class Cview_Buttons(SideButtonframe):
    def __init__(self, container, tx, lb,textwidget):
        super().__init__(container, textwidget)
        self.tx = tx
        self.text = textwidget
        self.lb = lb
        self.parent = container
  

        self.dir = tk.Button(self.fr_buttons, text="get dir", bd=8, command=lambda: self.newdirlist())
        self.dir.grid(row=14, column=0)

        self.btn_grab = tk.Button(self.fr_buttons, text="Send to ",bd=8, command=lambda: self.ggtxt(self.tx))
        self.btn_grab.grid(row=15, column=0)

   
        
       
      

    

    def listing(self,event=None):
        x = event.widget
        try:
            x = int(self.lb.curselection()[0])
            file = self.lb.get(x)
        except IndexError:
         
            v=(self.lb.get(x))
            v =  self.lb.curselection()[0]
            file = self.lb.get(v)
           
        with open(file, "r") as file:
            content = file.read()
            self.tx.delete("1.0", tk.END)
            self.tx.insert(tk.END, content)
            self.curtxt = content
            return self.curtxt

    def newdirlist(self):
      

        self.path = askdirectory()
        os.chdir(self.path)
        self.flist = os.listdir(self.path)
        self.lb.delete(0, tk.END)

        for self.item in self.flist:

            self.lb.insert(tk.END, self.item)
        return self.flist


    def showcontent(self,x, event=None):
        for i in self.lb.curselection():
            file = self.lb.get(i)
            with open(file, "r") as file:
                file = file.read()
                self.tx.delete("1.0", tk.END)
                self.tx.insert(tk.END, file)

            return


    def ggtxt(self, tx):
        self.tx = tx
        gettxt = self.tx.get("1.0", tk.END)
        self.text.insert(tk.END, gettxt)


   
    def run(self,listbox):

        self.file = self.listbox.get(ANCHOR)
        runpy.run_module(self.file)
        return

