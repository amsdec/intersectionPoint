class Line(object):
	
	def __init__(self, pointA, pointB):
		self.pointA = pointA
		self.pointB = pointB	

	def toString(self):
		return self.pointA.toString()	+ " a " + self.pointB.toString()