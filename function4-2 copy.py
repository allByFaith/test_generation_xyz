# Create a clear window with no element in it
import tkinter

class machineGUI:
    def __init__(self):
        myString = '\n   My Whole New World!   \n'
        # Create the main window widget. 
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window,text=myString)
        self.label.pack()

        # Enter the tkinter main loop. 
        tkinter.mainloop()

# Create an instance of the machineGUI class. 
my_gui = machineGUI()