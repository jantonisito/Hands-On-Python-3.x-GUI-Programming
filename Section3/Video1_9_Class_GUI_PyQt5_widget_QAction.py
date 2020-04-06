'''
Created on Mar 7, 2019
@author: Burkhard A. Meier
'''

# class inheriting from QMainWindow  
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
 

class GUI(QMainWindow):                 # inherit from QMainWindow
    def __init__(self): 
        super().__init__()              # initialize super class, which creates the window  
        self.initUI()                   # refer to window as 'self'
          
    def initUI(self):   
        self.setWindowTitle('PyQt5 GUI')     # call method
        self.resize(400, 300)                # resize window (width, height)
        self.add_widgets()
        
    def add_widgets(self):        
        self.statusBar().showMessage('Text in statusbar')
        
        menubar = self.menuBar()                # create menu bar
        file_menu = menubar.addMenu('File')     # add menu to menu bar
          
        new_action = QAction('New', self)       # create an Action      
        file_menu.addAction(new_action)         # add Action to menu
          
        new_action.setStatusTip('New File')     # statusBar updated
        
        #added Quit menu item 
        quit_action = QAction('Quit', self)
        quit_action.triggered.connect(qApp.quit)
        quit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(quit_action)
        

if __name__ == '__main__':     
    app = QApplication(sys.argv)        # create Application     
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt5 window
    sys.exit(app.exec_())               # execute the application


















