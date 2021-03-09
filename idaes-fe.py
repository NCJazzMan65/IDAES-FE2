#######################################################################
#                                                                     #
#               IDAES Flowsheet Editor (IDAES-FE)                     #
#                                                                     #
#  This program is a graphical interface for creating, editing, and   #
#  running process model flowsheets based on the DOE IDAES platform.  #
#                                                                     #
#  Author:  Timothy A. Fuller                                         #
#  Date:  3/7/2020                                                    #
#                                                                     #
#  Version:  1.0.0                                                    #
#                                                                     #
#######################################################################


# System module imports
import sys
import os

# PyQT imports
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


# Define main window class
class MainWindow(qtw.QMainWindow):

    # Initialize class
    def __init__(self):
        
        # Call initialization on parent object
        super().__init__()

        # Setup main window
        self.setWindowTitle("IDAES Flowsheet Editor")
        self.centralWidget = qtw.QWidget(self)
        self.resize(1024,768)
        

        # Show the main window
        self.show()


        



# Define main method
def main():

    # Create the application and open the main window
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


# Call main function on startup
if __name__ == '__main__':
    main()
