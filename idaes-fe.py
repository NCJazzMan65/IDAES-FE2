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
#  Revision Date:  4/12/2021                                          #
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
        self.resize(1024,768)

        # Create central widget
        self.mainarea = qtw.QWidget()
        self.setCentralWidget(self.mainarea)
        self.mainarea.setLayout(qtw.QHBoxLayout)

        # Create main menu
        self.create_main_menu()

        # Show the main window
        self.show()


    # Method to create main menu
    def create_main_menu(self):

        mainmenu = self.menuBar()

        # Add FILE menu
        file_menu = mainmenu.addMenu('File')

        # Add EDIT menu
        edit_menu = mainmenu.addMenu('Edit')

        # Add RUN menu
        run_menu = mainmenu.addMenu('Run')

        # Add View menu
        view_menu = mainmenu.addMenu('View')

        # Add Help menu
        help_menu = mainmenu.addMenu('Help')




# Define main method
def main():

    # Create the application and open the main window
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())


# Call main function on startup
if __name__ == '__main__':
    main()
