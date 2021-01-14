import re, requests
from bs4 import BeautifulSoup
import random

#beep boop

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton, QListWidget)

import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets

statedict = {"AL":"Alabama","AK":"Alaska","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","FL":"Florida","GA":"Georgia",
	"HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MD":"Maryland","MA":"Massachusetts",
	"MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico",
	"NY":"New York","NC":"North Carolina","ND":"North Dakota","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PA":"Pennsylvania","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota",
	"TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}
	#print(statedict['NJ'])


funfact={'Alabama': 'This state contains many significant landmarks from the Civil Rights Movement.', 'Alaska': 'This is the coldest state.', 
'Arizona': 'This state contains the most snake species.', 'Arkansas': 'Bill Clinton grew up in this state.', 
'California': 'This state is nicknamed the Golden State.', 'Colorado': 'This state is nicknamed the Centennial State.', 'Connecticut': 'This state is nicknamed the Constitution State.', 
'Delaware': "It's the second smallest state.", 
'Florida': 'This state is nicknamed the Sunshine State.', 'Georgia': 'The Olympics were held in this state.', 'Hawaii': 'The most recent state to be admitted to the Union.', 'Idaho': "Potatoes. That's all.", 
'Illinois': 'This state contains one of the largest cities in the country.', 'Indiana': 'This state is nicknamed the Hoosier State.', 
'Iowa': 'This state is mostly made up of farmland, and is known for its cornfields and plains.', 
'Kansas': 'Think about "The Wizard of Oz."', 
'Kentucky': 'This state is nicknamed the Bluegrass State.', 'Louisiana': 'This state is known for its French Quarter and Mardis Gras festivals.', 
'Maine': 'This state is home to Acadia National Park.', 'Maryland': 'This state is the setting for the movie "Hairspray."', 
'Massachusetts': 'Go Red Sox!', 'Michigan': 'This state is nicknamed the Wolverine State.', 
'Minnesota': 'This state contains the Mall of America.', 
'Mississippi': 'Elvis grew up in this state.', 'Missouri': "This state held the World's Fair in the early 1900s.", 'Montana': 'This state is home to Glacier National Park.', 
'Nebraska': 'This state is nicknamed the Cornhusker State.', 
'Nevada': "This state is home of the Hoover Dam.", 'New Hampshire': 'This state borders the Canadian province, Quebec.', 'New Jersey': 'This state is nicknamed the Garden State.', 
'New Mexico': "The Georgia O'Keeffe museum is in this state.", 
'New York': 'This state is nicknamed the Empire State.', 'North Carolina': 'This state is nicknamed the Tar Heel State.', 
'North Dakota': 'This state is nicknamed the Sioux State.', 
'Ohio': 'This state is bordered by Lake Erie.', 'Oklahoma': 'This state is nicknamed the Sooner State.', 'Oregon': 'This state is nicknamed the Beaver State.', 
'Pennsylvania': 'Think about the movie "Rocky"!', 'Rhode Island': 'This is the smallest state.', 
'South Carolina': "This state is where the Civil War's opening shots were fired.", 'South Dakota': 'This state has one of the smallest populations.', 
'Tennessee': 'This state is home to the Country Music Hall of Fame.', 
'Texas': 'Remember the Alamo.', 
'Utah': 'Roughly 60 percent of the state is Mormon.', 'Vermont': 'This state is a skiing and hiking destination.', 'Virginia': 'This state is nicknamed the Mother of Presidents.', 
'Washington': 'This state is home to the Space Needle.', 
'West Virginia': 'This state was formed when it split from another state in order to avoid joining the Confederacy.',
 'Wisconsin': 'This state is nicknamed America’s Dairyland.', 'Wyoming': 'Yellowstone National Park is located in this state.'}




states=['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 
'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 
'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 
'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']


reigondict={"Connecticut":"New England","Maine":"New England","Massachusetts":"New England","New Hampshire":"New England","Rhode Island":"New England","Vermont":"New England",
"Delaware":"the North East","Maryland":"the North East","New Jersey":"the North East","New York":"the North East","Pennsylvania":"the North East",
"Alabama":"the South","Arkansas":"the South","Florida":"the South","Georgia":"the South","Kentucky":"the South",
"Louisiana":"the South","Mississippi":"the South","Missouri":"the South","North Carolina":"the South","South Carolina":"the South",
"Tennessee":"the South","Virginia":"the South","West Virginia":"the South",
"Illinois":"the Midwest","Indiana":"the Midwest","Iowa":"the Midwest","Kansas":"the Midwest","Michigan":"the Midwest","Minnesota":"the Midwest",
"Nebraska":"the Midwest","North Dakota":"the Midwest","Ohio":"the Midwest","South Dakota":"the Midwest","Wisconsin":"the Midwest",
"Arizona":"the Southwest","New Mexico":"the Southwest","Oklahoma":"the Southwest", "Texas":"the Southwest",
"Alaska":"the West","California":"the West","Colorado":"the West","Hawaii":"the West","Idaho":"the West",
"Montana":"the West","Nevada":"the West","Oregon":"the West","Utah":"the West","Washington":"the West","Wyoming":"the West"}




iconroot = os.path.dirname(__file__)


class Grid(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Grid, self).__init__(parent)
		self.setWindowTitle("State Quarters Quiz")
		self.setMinimumHeight(900) 
		self.setMinimumWidth(800)  


		self.prompt=QLabel(f'You have 5 tries to guess the state for each state quarter! Good luck!')
		self.prompt.setAlignment(QtCore.Qt.AlignCenter)

		self.startButton=QPushButton("Start")       
		self.startButton.setStyleSheet("font: bold; font-size: 125%; background-color: white")        
		self.startButton.clicked.connect(self.startbutton_clicked)
		self.vlay1 = QtWidgets.QVBoxLayout(self)
		self.vlay1.addWidget(self.prompt)
		self.vlay1.addWidget(self.startButton)



	def startbutton_clicked(self):
		self.prompt.deleteLater()
		self.startButton.deleteLater()
		self.click_count=5
		self.tries=[]
		self.scoreint=0
		self.correct=0

		self.random50=random.sample(range(50),50)
		self.index=0


		self.score=QLabel(f'Score: {self.scoreint}')
		

		self.attempts=QLabel(f'Attempts Remaining: {self.click_count}')
		self.attempts.setStyleSheet("font: bold; font-size: 125%")   

		self.statesremaining=QLabel(f'States Remaining: 50')
		self.statesremaining.setAlignment(QtCore.Qt.AlignRight)


		self.hint=QLabel("")
		self.hint.setStyleSheet("font: bold; font-size: 125%")   
		self.hint2=QLabel("")
		self.hint2.setStyleSheet("font: bold; font-size: 125%") 
		#self.hint.hide()
		#self.hint2.hide()  
		hlay1 = QtWidgets.QHBoxLayout()
		hlay1.addWidget(self.score)
		hlay1.addWidget(self.statesremaining)
		self.vlay1.addLayout(hlay1)

		self.vlay1.addWidget(self.prompt)
		self.vlay1.addWidget(self.attempts)
		self.vlay1.addWidget(self.hint)
		self.vlay1.addWidget(self.hint2)

		self.label = QtWidgets.QLabel()
		self.pixmap = QtGui.QPixmap(os.path.join(iconroot, f"images/state{self.random50[self.index]}.png"))


		self.label.resize(700, 700)
		self.label.setPixmap(self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))

		self.vlay1.addWidget(self.label)

		

		self.hlay2 = QtWidgets.QHBoxLayout()
		self.state = QtWidgets.QLabel('State:')
		self.state.setStyleSheet("font: bold; font-size: 125%")
		self.hlay2.addWidget(self.state)

		self.enterstate=QLineEdit()
		self.enterstate.setStyleSheet("font: bold; font-size: 125%")
		self.enterstate.textChanged.connect(self.clean)       

		self.hlay2.addWidget(self.enterstate)

		self.Button=QPushButton("Done")       
		self.Button.setStyleSheet("font: bold; font-size: 125%; background-color: white")        
		self.Button.setEnabled(True)
		self.Button.clicked.connect(self.button1_clicked)
		self.enterstate.returnPressed.connect(self.button1_clicked)
		self.hlay2.addWidget(self.Button)

		self.refresh=QPushButton("Next")
		self.refresh.setStyleSheet("font: bold; font-size: 125%; background-color: white")
		self.refresh.clicked.connect(self.button2_clicked)        
		self.hlay2.addWidget(self.refresh)

		self.vlay1.addLayout(self.hlay2)


	def button1_clicked(self):
		self.click_count-=1

		self.tries.append(self.enterstate.text())

		state=self.enterstate.text()
		if len(state)==2:
			if state.upper() in statedict.keys():
				state=statedict[state.upper()]

		if state.lower()==states[self.random50[self.index]].lower():
			self.correct+=1
			self.attempts.setText(f'Congrats!')
			self.attempts.setStyleSheet("font: bold; font-size: 125%; color: black")
			self.enterstate.setStyleSheet("font: bold; font-size: 125%; background-color: green")
			#self.enterstate.setEnabled(False)

			if self.click_count==4:
				self.scoreint+=100
				self.score.setText(f'Score: {self.scoreint}')

			if self.click_count==3:
				self.scoreint+=75
				self.score.setText(f'Score: {self.scoreint}')

			if self.click_count==2:
				self.scoreint+=50
				self.score.setText(f'Score: {self.scoreint}')

			if self.click_count==1:
				self.scoreint+=25
				self.score.setText(f'Score: {self.scoreint}')

			if self.click_count==0:
				self.scoreint+=5
				self.score.setText(f'Score: {self.scoreint}')


		else:
			self.attempts.setText(f"Attempts Remaining: {self.click_count}. You've already tried {(', '.join(self.tries))}.")
			self.enterstate.setStyleSheet("font: bold; font-size: 125%; background-color: red")
			self.enterstate.setText("")

			if self.click_count==1:
				self.attempts.setStyleSheet("font: bold; font-size: 125%; background-color: red; color: black")

			if self.click_count == 2:
				self.attempts.setStyleSheet("font: bold; font-size: 125%; color: red")
				self.hint2.show()
				self.hint2.setText(f'Hint 2: {funfact[states[self.random50[self.index]]]}')

			if self.click_count == 3:
				self.attempts.setStyleSheet("font: bold; font-size: 125%; color: red")
				self.hint.show()
				self.hint.setText(f'Hint 1: This state is located in {reigondict[states[self.random50[self.index]]]}.')

			if self.click_count==0:

				self.enterstate.setText(f'{states[self.random50[self.index]]}')
				self.enterstate.setEnabled(False)


	def button2_clicked(self):
		self.index+=1
		self.statesremaining.setText(f'States Remaining: {50-self.index}')	
		self.enterstate.setEnabled(True)
		self.tries=[]
		self.attempts.setStyleSheet("font: bold; font-size: 125%; color: black")
		self.attempts.setStyleSheet("font: bold; font-size: 125%")
		self.click_count=5
		self.attempts.setText(f'Attempts Remaining: {self.click_count}')
		self.hint.setText("")
		self.hint2.setText("")
		self.label.clear()
		self.enterstate.setStyleSheet("font: bold; font-size: 125%; background-color: white")
		self.enterstate.setText("") 

		if self.index<50:
			self.pixmap = QtGui.QPixmap(os.path.join(iconroot, f"images/state{self.random50[self.index]}.png"))

		#endscreen
		if self.index>=50:
			self.attempts.deleteLater()
			self.pixmap = QtGui.QPixmap(os.path.join(iconroot, "images/complete.png"))
			self.Button.deleteLater()
			self.refresh.deleteLater()
			self.hint.hide()
			self.hint2.hide()
			self.enterstate.hide()
			self.state.hide()
			self.statesremaining.hide()
			self.score.setText(f"Final Score: {self.scoreint}. \nYou've completed all 50 states! You got {self.correct}/50 correct")
			self.score.setAlignment(QtCore.Qt.AlignCenter)

			self.score.setStyleSheet("font: bold; font-size: 125%")
			self.space=QLabel("     ")
			self.vlay1.addWidget(self.space)




		self.label.resize(700, 700)
		self.label.setPixmap(self.pixmap.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))




	def clean(self):        
		if self.enterstate.text() != "":
			self.enterstate.setStyleSheet("font: bold; font-size: 125%; background-color: white")


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	im = Grid()
	im.show()
	sys.exit(app.exec_())



