##############################################
#                                            #
#       IDAES Editor Flowsheet Class         #
#                                            #
#  This class represents an IDAES flowsheet  #
#  upon which a an IDAES model is built.     #
#  The flowsheet holds the graphic elements  #
#  representing different unit operation     #
#  models and streams connecting the unit    #
#  models.                                   #
#                                            #
#  Author:  T.A. Fulelr                      #
#  Date:  2022-03-013                        #
#  Revision: 0                               #
#                                            #
##############################################  

"""IDAES Flowsheet Class"""

import sys
import os

# PyQT imports
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


class Flowsheet(qtw.QWidget):

    # Initialize the class
    def __init__(self):

        # Call initialization on parent object
        super().__init__()

        # Allow drag-drop operations
        self.setAcceptDrops(True)

        # Add a blank image as the canvas for drawing
        self.canvas = qtg.QImage()
