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

from code_ctrl import enable_betafeatures

class scan_ribbon(QTabWidget):
	def goto_page(self,page):
		self.blockSignals(True)
		for i in range(0,self.count()):
				if self.tabText(i)==page:
					self.setCurrentIndex(i)
					break
		self.blockSignals(False)
		
	def scan(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.tb_new = QAction(QIcon_load("document-new"), wrap_text(_("New scan"),2), self)
		toolbar.addAction(self.tb_new)

		self.tb_delete = QAction(QIcon_load("edit-delete"), wrap_text(_("Delete scan"),3), self)
		toolbar.addAction(self.tb_delete)

		self.tb_clone = QAction(QIcon_load("clone"), wrap_text(_("Clone scan"),3), self)
		toolbar.addAction(self.tb_clone)

		self.tb_rename = QAction(QIcon_load("rename"), wrap_text(_("Rename scan"),3), self)
		toolbar.addAction(self.tb_rename)


		spacer = QWidget()
		spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		toolbar.addWidget(spacer)

		self.home_help = QAction(QIcon_load("internet-web-browser"), _("Help"), self)
		toolbar.addAction(self.home_help)

		return toolbar

	def simulations(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.tb_simulate = QAction(QIcon_load("build_play2"), wrap_text(_("Run scan"),2), self)
		toolbar.addAction(self.tb_simulate)


		self.tb_stop = QAction(QIcon_load("media-playback-pause"), wrap_text(_("Stop"),3), self)
		toolbar.addAction(self.tb_stop)

		toolbar.addSeparator()

		self.tb_plot = QAction(QIcon_load("plot"), wrap_text(_("Plot"),4), self)
		toolbar.addAction(self.tb_plot)
	
		self.tb_plot_time = QAction(QIcon_load("plot_time"), wrap_text(_("Time domain plot"),6), self)
		toolbar.addAction(self.tb_plot_time)


		self.box_widget=QWidget()
		self.box=QVBoxLayout()
		self.box_widget.setLayout(self.box)
		self.box_tb0=QToolBar()
		self.box_tb0.setIconSize(QSize(32, 32))
		self.box.addWidget(self.box_tb0)
		self.box_tb1=QToolBar()
		self.box_tb1.setIconSize(QSize(32, 32))
		self.box.addWidget(self.box_tb1)
		
		self.tb_build = QAction(QIcon_load("cog"), wrap_text(_("Build scan"),2), self)
		self.box_tb0.addAction(self.tb_build)

		self.tb_rerun = QAction(QIcon_load("play-green"), wrap_text(_("Rerun"),2), self)
		self.box_tb0.addAction(self.tb_rerun)

		self.tb_zip = QAction(QIcon_load("package-x-generic"), wrap_text(_("Archive simulations"),2), self)
		self.box_tb0.addAction(self.tb_zip)


		self.tb_clean = QAction(QIcon_load("clean"), wrap_text(_("Clean simulation"),4), self)
		self.box_tb1.addAction(self.tb_clean )

		self.tb_run_all = QAction(QIcon_load("forward2"), wrap_text(_("Run all scans"),3), self)
		self.box_tb1.addAction(self.tb_run_all)

		toolbar.addWidget(self.box_widget)
		
		return toolbar

	def nested(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.menu_run_nested = QAction(QIcon_load("nested"), wrap_text(_("Build nested simulation"),5), self)
		toolbar.addAction(self.menu_run_nested)

		return toolbar

	def advanced(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.menu_plot_fits = QAction(QIcon_load("scan2"), wrap_text(_("Plot fits"),5), self)
		toolbar.addAction(self.menu_plot_fits)

		self.sim_no_gen = QAction(QIcon_load("forward"), wrap_text(_("Run simulation no generation"),5), self)
		toolbar.addAction(self.sim_no_gen)

		self.single_fit = QAction(QIcon_load("forward"), wrap_text(_("Run single fit"),5), self)
		toolbar.addAction(self.single_fit)

		self.clean_unconverged = QAction(QIcon_load("clean"), wrap_text(_("Clean unconverged simulation"),5), self)
		toolbar.addAction(self.clean_unconverged)

		self.clean_sim_output = QAction(QIcon_load("forward"), wrap_text(_("Clean simulation output"),5), self)
		toolbar.addAction(self.clean_sim_output)

		self.push_unconverged_to_hpc = QAction(QIcon_load("forward"), wrap_text(_("Push unconverged to hpc"),5), self)
		toolbar.addAction(self.push_unconverged_to_hpc)

		self.change_dir = QAction(QIcon_load("forward"), wrap_text(_("Change dir"),5), self)
		toolbar.addAction(self.change_dir)

		self.report = QAction(QIcon_load("office-calendar"), wrap_text(_("Report"),5), self)
		toolbar.addAction(self.report)

		return toolbar

	def ml(self):
		toolbar = QToolBar()
		toolbar.setToolButtonStyle( Qt.ToolButtonTextUnderIcon)
		toolbar.setIconSize(QSize(42, 42))

		self.tb_ml_build_vectors = QAction(QIcon_load("ml"), wrap_text(_("Build vectors"),4), self)
		toolbar.addAction(self.tb_ml_build_vectors)


		return toolbar

	def readStyleSheet(self,fileName):
		css=None
		file = QFile(fileName)
		if file.open(QIODevice.ReadOnly) :
			css = file.readAll()
			file.close()
		return css

	def update(self):
		print("update")
		#self.device.update()
		#self.simulations.update()
		#self.configure.update()
		#self.home.update()

	def callback_about_dialog(self):
		dlg=about_dlg()
		dlg.exec_()

	def __init__(self):
		QTabWidget.__init__(self)
		self.setMaximumHeight(130)
		#self.setStyleSheet("QWidget {	background-color:cyan; }")

		self.about = QToolButton(self)
		self.about.setText(_("About"))
		self.about.pressed.connect(self.callback_about_dialog)

		self.setCornerWidget(self.about)

		w=self.scan()
		self.addTab(w,_("Scan"))
		
		w=self.simulations()
		self.addTab(w,_("Simulations"))


		w=self.advanced()
		if enable_betafeatures()==True:
			self.addTab(w,_("Advanced"))

		w=self.nested()
		if enable_betafeatures()==True:
			self.addTab(w,_("Nested"))

		w=self.ml()
		if enable_betafeatures()==True:
			self.addTab(w,_("ML"))

		sheet=self.readStyleSheet(os.path.join(get_css_path(),"style.css"))
		if sheet!=None:
			sheet=str(sheet,'utf-8')
			self.setStyleSheet(sheet)

