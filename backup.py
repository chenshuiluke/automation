class Backup:
	def __init__(self):
		self.origin = None
		self.destination = None
	def setDestination(self, newDestination : string):
		self.destination = newDestination
	def setOrigin(self, newOrigin : string):
		self.origin = newOrigin
