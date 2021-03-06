# -*- coding: utf-8 -*-
#    General-purpose Photovoltaic Device Model - a drift diffusion base/Shockley-Read-Hall
#    model for 1st, 2nd and 3rd generation solar cells.
#    Copyright (C) 2012-2017 Roderick C. I. MacKenzie <r.c.i.mackenzie@googlemail.com>
#
#	https://www.gpvdm.com
#	Room B86 Coates, University Park, Nottingham, NG7 2RD, UK
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License v2.0, as published by
#    the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os

from dump_io import dump_io
from tb_item_sim_mode import tb_item_sim_mode
from tb_item_sun import tb_item_sun

from code_ctrl import enable_betafeatures
from cal_path import get_css_path

#qt
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt,QFile,QIODevice
from PyQt5.QtWidgets import QWidget,QSizePolicy,QVBoxLayout,QHBoxLayout,QPushButton,QDialog,QFileDialog,QToolBar,QMessageBox, QLineEdit, QToolButton
from PyQt5.QtWidgets import QTabWidget

from icon_lib import QIcon_load

from about import about_dlg

from util import wrap_text

class plot_ribbon(QTabWidget):
		
	def plot(self):
		self.plot_toolbar = QToolBar()
		self.plot_toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		self.plot_toolbar.setIconSize(QSize(42, 42))

		return self.plot_toolbar


	def file(self):
		self.file_toolbar = QToolBar()
		self.file_toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		self.file_toolbar.setIconSize(QSize(42, 42))

		self.tb_save = QAction(QIcon_load("document-save-as"), _("Save"), self)
		self.file_toolbar.addAction(self.tb_save)

		self.tb_save_as = QAction(QIcon_load("document-save-as"), _("Save as"), self)
		self.file_toolbar.addAction(self.tb_save_as)

		return self.file_toolbar

	def color(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.tb_color_black = QAction(QIcon_load("black"), _("Black"), self)
		toolbar.addAction(self.tb_color_black)

		self.tb_color_rainbow = QAction(QIcon_load("rainbow"), _("Rainbow"), self)
		toolbar.addAction(self.tb_color_rainbow)

		return toolbar

	def scale(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.tb_scale_autoscale = QAction(QIcon_load("plot_log_x"), _("Autoscale"), self)
		toolbar.addAction(self.tb_scale_autoscale)

		self.tb_scale_log_y = QAction(QIcon_load("plot_log_x"), _("Set log scale y"), self)
		toolbar.addAction(self.tb_scale_log_y)

		self.tb_scale_log_x = QAction(QIcon_load("plot_log_x"), _("Set log scale x"), self)
		toolbar.addAction(self.tb_scale_log_x)


		return toolbar

	def math(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.math_subtract_first_point = QAction(QIcon_load("plot_log_x"), _("Subtract first point"), self)
		toolbar.addAction(self.math_subtract_first_point)

		self.math_add_min_point = QAction(QIcon_load("plot_log_x"), _("Add min point"), self)
		toolbar.addAction(self.math_add_min_point)

		self.math_invert_y_axis = QAction(QIcon_load("plot_log_x"), _("Invert y-axis"), self)
		toolbar.addAction(self.math_invert_y_axis)

		self.math_norm_y_to_one = QAction(QIcon_load("plot_log_x"), _("Norm to 1.0 y"), self)
		toolbar.addAction(self.math_norm_y_to_one)

		self.math_norm_to_peak_of_all_data = QAction(QIcon_load("plot_log_x"), _("Norm to peak of all data"), self)
		toolbar.addAction(self.math_norm_to_peak_of_all_data)

		self.math_heat_map = QAction(QIcon_load("plot_log_x"), _("Heat map"), self)
		toolbar.addAction(self.math_heat_map)

		self.math_heat_map_edit = QAction(QIcon_load("plot_log_x"), _("Heat map edit"), self)
		toolbar.addAction(self.math_heat_map_edit)

		return toolbar

	def readStyleSheet(self,fileName):
		css=None
		file = QFile(fileName)
		if file.open(QIODevice.ReadOnly) :
			css = file.readAll()
			file.close()
		return css

	def __init__(self):
		QTabWidget.__init__(self)
		self.setMaximumHeight(130)
		#self.setStyleSheet("QWidget {	background-color:cyan; }")


		w=self.plot()
		self.addTab(w,_("Plot"))

		w=self.file()
		self.addTab(w,_("File"))

		w=self.color()
		self.addTab(w,_("Color"))

		w=self.scale()
		self.addTab(w,_("Scale"))

		w=self.math()
		self.addTab(w,_("Math"))

		sheet=self.readStyleSheet(os.path.join(get_css_path(),"style.css"))
		if sheet!=None:
			sheet=str(sheet,'utf-8')
			self.setStyleSheet(sheet)

