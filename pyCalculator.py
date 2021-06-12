#python GUI
import parser
from tkinter import *
import _tkinter
#Creating a window
root = Tk()
#Creating a title for the window
root.title("Calculator")
#To open as full screen
# root.attributes('-fullscreen',True)

#get variables function to display the enterned number
i=0
def get_variables(num):
   global i
   display.insert(i,num)
   i+=1
#for operators
def get_operation(operator):
    global i
    display.insert(i,operator)
    i+=1

def clearAll():
    display.delete(0,END)

def calculate():
 full_string = display.get()
 try:
     a = parser.expr(full_string).compile()
     result = eval(a)
     clearAll()
     display.insert(0,result)
 except Exception:
     clearAll()
     display.insert(0,"Error")



#Creating UI

#Creating a window
display = Entry(root)
display.grid(columnspan = '4',rowspan = '2',sticky=N+E+W+S)

#Creating buttons
Button(root,text = '1', command = lambda : get_variables(1)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text = '2', command = lambda : get_variables(2)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text = '3', command = lambda : get_variables(3)).grid(row=2,column=2,sticky=N+S+E+W)

Button(root,text = '4', command = lambda : get_variables(4)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text = '5', command = lambda : get_variables(5)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text = '6', command = lambda : get_variables(6)).grid(row=3,column=2,sticky=N+S+E+W)

Button(root,text = '7', command = lambda : get_variables(7)).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text = '8', command = lambda : get_variables(8)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text = '9', command = lambda : get_variables(9)).grid(row=4,column=2,sticky=N+S+E+W)

Button(root,text = 'AC', command = lambda : clearAll()).grid(row=5,column=0,sticky=N+S+E+W)
Button(root,text = '0', command = lambda : get_variables(0)).grid(row=5,column=1,sticky=N+S+E+W)
Button(root,text = '.', command = lambda : get_variables('.')).grid(row=5,column=2,sticky=N+S+E+W)

Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root,text="-",command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root,text="*",command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root,text="/",command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)

Button(root,text="=",command= lambda :calculate()).grid(columnspan=4, sticky=N+S+E+W)


#Creating a endless loop
root.mainloop()
