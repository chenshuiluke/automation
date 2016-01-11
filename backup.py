import json
import os
class Backup:
	def __init__(self):
		self.name = ""
		self.origin = ""
		self.destination = ""
	def setDestination(self, newDestination : str):
		self.destination = newDestination
	def setOrigin(self, newOrigin : str):
		self.origin = newOrigin

	def getUserInput(self):
			self.name = input("Please enter the name of the backup.")
			while not os.path.isdir(self.origin):
				self.origin = input("Please enter the name of the directory.")
			while not os.path.isdir(self.destination) and self.destination != self.origin:
				self.destination = input("Please enter the destination of the backup.")

	def initFromJson(self, json):
		self.name = json['name']
		self.origin = json['origin']
		self.destination = json['destination']

	def returnJson(self):
		print(json.dumps(self.__dict__))
		return json.dumps(self.__dict__)
