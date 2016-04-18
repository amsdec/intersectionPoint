class Ecuation(object):

	def __init__(self, multiplicadorDeX, multiplicadorDeY, sumando):
		self.multiplicadorDeY = multiplicadorDeY
		self.multiplicadorDeX = multiplicadorDeX
		self.sumando = sumando

	def toString(self):
		ecuacionLinea = str(self.multiplicadorDeX) + "x + " + str(self.sumando) + " = " + str(self.multiplicadorDeY) + "y "
		return ecuacionLinea

	def despejarY():
		despejeY = "y = (" + str(getMultiplierOfXIn(linea)) + "x + " + str(getSumandos(linea)) + ")/" + str(getMultiplierOfYIn(linea))
		print("Despejando Y en la ecuacion...")
		print despejeY

class EquationResolver(object):

	def findValue(self, equationOne, equationTwo):		
		return (equationTwo.sumando*equationOne.multiplicadorDeY - equationOne.sumando*equationTwo.multiplicadorDeY)/(equationOne.multiplicadorDeX*equationTwo.multiplicadorDeY - equationOne.multiplicadorDeY*equationTwo.multiplicadorDeX)