from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog as fd
from numpy.core.defchararray import title

class PdfTool(object):
	def __init__(self, master):
		frame = Frame(master)
		frame.grid()
		self.file_path = ""
		self.options = ["Text","Docx","Picture","Pdf"]
		
		self.selection_frame = LabelFrame(root,text="PDF Convertion Tool",height=100,width=100)
		self.selection_frame.grid(column=0, row="0",padx="10", pady="10")
		
		self.file_label = Label(self.selection_frame,text="file: ")
		self.file_label.grid(column=0,row=0,padx="5")
		self.file_entry = Entry(self.selection_frame,width=25)
		self.file_entry.grid(column=1, row="0",padx=5)
		self.set_botton = Button(self.selection_frame,text = "Set") 
		self.set_botton.grid(column=2, row=0, padx=5)

		self.file_label = Label(self.selection_frame, text="Format: ")
		self.file_label.grid(column=0, row=1,padx=5)
		self.from_menu = ttk.Combobox(self.selection_frame,values=self.options)
		self.from_menu.grid(column=1,row=1,padx=5)
		self.from_menu.current(0)
		self.convert_botton = Button(self.selection_frame, text="Convert: ")
		self.convert_botton.grid(column=2,row=1)

		self.result_label = Label(self.selection_frame, text="")
		self.result_label.grid(column=0,row=2,columnspan=3)


root = Tk()
root.title = "Pdf Tool"
PdfTool(root)
root.mainloop()