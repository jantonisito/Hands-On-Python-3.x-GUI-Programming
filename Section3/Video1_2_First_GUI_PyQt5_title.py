'''
Created on Mar 7, 2019
@author: Burkhard A. Meier
'''

import sys 
from PyQt5.QtWidgets import QApplication, QWidget
 
app = QApplication(sys.argv)        # sys.argv accepts arguments when run from the command line
gui = QWidget()                     # creates top-level window

#debug
#print("\n".join(sys.argv))

if(len(sys.argv) > 0):
    win_title = sys.argv[1]
else:
    win_title = 'PyQt5 GUI'
gui.setWindowTitle(win_title)     # give our Window a title

gui.show()                          # have to call show() to make it visible 
sys.exit(app.exec_())               # run the application; PyQt5 exec_ ends with an underscore






















