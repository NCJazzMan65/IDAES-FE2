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

        # Create main menu
        self.create_main_menu()

        # Create main layout
        self.main_grid = qtw.QGridLayout()
        self.mainarea.setLayout(self.main_grid)
        self.create_main_areas()

        # Create the status bar
        self.status_bar = qtw.QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Flowsheet Editor Ready")

        # Show the main window
        self.show()


    # Method to create main display areas
    def create_main_areas(self):

        # Create flowsheet tab
        self.flowsheet_tab = qtw.QTabWidget()
        flowsheet = qtw.QWidget()
        self.flowsheet_tab.addTab(flowsheet, 'Flowsheet 1')
        self.main_grid.addWidget(self.flowsheet_tab, 0, 0)

        # Create properties area
        self.prop_area = qtw.QWidget()
        self.main_grid.addWidget(self.prop_area, 0, 1)

        # Create unit model tabs
        self.unit_model_tab = qtw.QTabWidget(tabPosition = qtw.QTabWidget.South)

        terminators = qtw.QWidget()
        terminator_layout = qtw.QHBoxLayout()
        terminators.setLayout(terminator_layout)
        feed_block = qtw.QLabel(self)
        feed_block.setFixedSize(100,75)
        feed_block_pix = qtg.QPixmap('idaes_graphics/Feed_Block_Icon.png')
        feed_block.setPixmap(feed_block_pix)
        terminator_layout.addWidget(feed_block)
        prod_block = qtw.QLabel(self)
        prod_block.setFixedSize(100,75)
        prod_block_pix = qtg.QPixmap('idaes_graphics/Product_Block_Icon.png')
        prod_block.setPixmap(prod_block_pix)
        terminator_layout.addWidget(prod_block)
        #terminator_blank = qtw.QWidget()
        #terminator_layout.addWidget(terminator_blank)

        reactors = qtw.QWidget()
        reactor_layout = qtw.QHBoxLayout()
        reactors.setLayout(reactor_layout)
        equil_reactor = qtw.QLabel(self)
        pixmap = qtg.QPixmap('idaes_graphics/Equil_Reactor_Icon.png')
        equil_reactor.setPixmap(pixmap)
        reactor_layout.addWidget(equil_reactor)

        self.unit_model_tab.addTab(terminators, 'Terminators')
        self.unit_model_tab.addTab(reactors, 'Reactors')
        self.main_grid.addWidget(self.unit_model_tab, 1, 0, 2, 2)
        

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
