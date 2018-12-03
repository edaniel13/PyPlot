#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui

from MainForm import Ui_MainWindow 

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random

class MainForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    # a figure instance to plot on
    self.figure = Figure()

    # this is the Canvas Widget that displays the `figure`
    # it takes the `figure` instance as a parameter to __init__
    self.canvas = FigureCanvas(self.figure)

    # this is the Navigation widget
    # it takes the Canvas widget and a parent
    self.toolbar = NavigationToolbar(self.canvas, self)

    self.ui.verticalLayout_2.addWidget(self.toolbar)
    self.ui.verticalLayout_2.addWidget(self.canvas)

    self.ui.pushButton.clicked.connect(self.plot)

  def plot(self):
      ''' plot some random stuff '''
      # random data
      data = [random.random() for i in range(10)]

      # create an axis
      ax = self.figure.add_subplot(111)

      # discards the old graph
      ax.clear()

      # plot data
      ax.plot(data, '*-')

      # refresh canvas
      self.canvas.draw()

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MainForm()
  myapp.show()
  sys.exit(app.exec_())

