#    General-purpose Photovoltaic Device Model - a drift diffusion base/Shockley-Read-Hall
#    model for 1st, 2nd and 3rd generation solar cells.
#    Copyright (C) 2012 Roderick C. I. MacKenzie <r.c.i.mackenzie@googlemail.com>
#
#	www.gpvdm.com
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
from cal_path import get_image_file_path
import webbrowser

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QProgressBar,QLabel,QDesktopWidget,QToolBar,QHBoxLayout,QAction,QSizePolicy
from PyQt5.QtGui import QPixmap

my_help_class=None

class help_data():
	def __init__(self,token,icon,text):
		self.token=token
		self.icon=icon
		self.text=text

class help_class(QWidget):
	def move_window(self):
		shape=QDesktopWidget().screenGeometry()

		w=shape.width()
		h=shape.height()
		win_w=self.frameGeometry().width()
		win_h=self.frameGeometry().height()

		x=w-win_w
		y=50
		self.move(x,y)

	def help_show(self):
		self.show()
		self.move_window()

	def toggle_visible(self):
		if self.isVisible()==True:
			self.setVisible(False)
		else:
			self.setVisible(True)

		self.move_window()

	def init(self):
		QWidget.__init__(self)
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
		self.setFixedSize(400,160)

		self.setStyleSheet(" padding:0px; margin-top:0px; margin-bottom:0px")
		#; border:2px solid rgb(0, 0, 0); 

		self.last=[]
		self.pos=-1

		self.move_window()
		self.vbox = QVBoxLayout()

		#self.vbox.setAlignment(Qt.AlignTop)
		self.box=[]
		self.image=[]
		self.label=[]
		for i in range(0,5):
			l=QHBoxLayout()
			label=QLabel()
			label.setWordWrap(True)
	
			image=QLabel()
			image.setFixedWidth(48)

			self.box.append( QWidget())
			self.image.append(image)
			label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
			self.label.append(label)

			self.box[i].setLayout(l)
			self.box[i].setFixedSize(380,80)
			l.addWidget(self.image[i])
			l.addWidget(self.label[i])

		toolbar=QToolBar()
		toolbar.setIconSize(QSize(48, 48))

		new_sim = QAction(QIcon(os.path.join(get_image_file_path(),"left.png")), 'Back', self)
		new_sim.setStatusTip(_("Make a new simulation"))
		new_sim.triggered.connect(self.callback_back)
		toolbar.addAction(new_sim)

		open_sim = QAction(QIcon(os.path.join(get_image_file_path(),"right.png")), 'Next', self)
		open_sim.setStatusTip(_("Open a simulation"))
		open_sim.triggered.connect(self.callback_forward)
		toolbar.addAction(open_sim)


		spacer = QWidget()
		spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		toolbar.addWidget(spacer)


		self.undo = QAction(QIcon(os.path.join(get_image_file_path(),"www.png")), 'Online help', self)
		self.undo.setStatusTip(_("On line help"))
		self.undo.triggered.connect(self.on_line_help)
		toolbar.addAction(self.undo)

		self.undo = QAction(QIcon(os.path.join(get_image_file_path(),"close.png")), 'Hide', self)
		self.undo.setStatusTip(_("Close"))
		self.undo.triggered.connect(self.callback_close)
		toolbar.addAction(self.undo)

		#self.status_bar = gtk.Statusbar()
		#self.context_id = self.status_bar.get_context_id("Statusbar example")
		#self.status_bar.show()
		#self.tooltips.set_tip(self.qe_button, "Quantum efficiency")


		self.vbox.addWidget(toolbar)

		for i in range(0,5):
			self.vbox.addWidget(self.box[i])

		self.vbox.addStretch()

		self.setLayout(self.vbox)
		self.show()


	def callback_close(self,widget):
		self.toggle_visible()

	def callback_forward(self,widget):
		self.pos=self.pos+1
		if self.pos>=len(self.last):
			self.pos=len(self.last)-1

		self.update()

	def callback_back(self,widget):
		self.pos=self.pos-1
		if self.pos<0:
			self.pos=0
		#print self.pos,self.last_icons
		self.update()

	def on_line_help(self,widget):
		webbrowser.open('http://www.gpvdm.com/man/index.html')

	def update(self):
		for i in range(0,5):
			self.box[i].hide()

		for i in range(0,int(len(self.last[self.pos])/2)):
			pixmap = QPixmap(os.path.join(get_image_file_path(),self.last[self.pos][i*2]))
			self.image[i].setPixmap(pixmap)
			self.label[i].setText(self.last[self.pos][i*2+1]+"\n")
			self.box[i].show()
			#self.image[i].show()

		#self.forward.set_sensitive(True)
		#self.back.set_sensitive(True)

		#if self.pos==0:
		#	self.back.set_sensitive(False)

		#if self.pos==len(self.last)-1:
		#	self.forward.set_sensitive(False)

		#self.status_bar.push(self.context_id, str(self.pos)+"/"+str(len(self.last)-1))

	def help_set_help(self,array):
		add=True
		if len(self.last)!=0:
			if self.last[self.pos][1]==array[1]:
				add=False

		if add==True:
			self.pos=self.pos+1
			self.last.append(array)
		self.update()
		self.resize(300, 150)
		self.move_window()

	def help_append(self,array):
		self.last[self.pos-1]=self.last[self.pos-1] + array
		self.update()
		self.resize(300, 150)
		self.move_window()


def help_init():
	global my_help_class
	my_help_class=help_class()
	my_help_class.init()

def help_window():
	global my_help_class
	return my_help_class


