#############################################################################
#                                                                           #
#                       IDAES Reactor Unit Models                           #
#                                                                           #
#  This file contains several different reactor unit model widgets used in  #
#  the IDAES Flowsheet Editor program. These reactor model widgets contain  #
#  methods for specifying the configuration of the specific reactor and     #
#  reactor and methods for supporting drag-drop operations on the           #
#  flowsheet.                                                               #
#                                                                           #
#  Unit model widgets included in this file are:                            #
#    - Continuous Stirred Tank Reactor                                      #
#    - Equilibrium Reactor                                                  #
#    - Gibbs Reactor                                                        #
#    - Plug Flow Reactor                                                    #
#    - Stoichionetric (Yield) Reactor                                       #
#                                                                           #
#  Author:  Timothy A. Fuller                                               #
#  Date:  4/12/2021                                                         #
#                                                                           #
#  Version:  1.0.0                                                          #
#                                                                           #
#  Revision Date:  4/12/2021                                                #
#                                                                           #
#############################################################################

"""
Reactor unit operations model widgets for the IDAES Flowsheet Editor
"""


# System imports
import sys
import os

# PyQT imports
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw


# Define equilibrium reactor class
class EquilReactor(qtw.QPushButton):

    # Class constructor
    def __init__(self):

        super().__init__()