import Ecuation

class EquationResolver(object):

	def findValue(self, equationOne, equationTwo):
		divisor = equationTwo.sumando*equationOne.multiplicadorDeY - equationOne.sumando*equationTwo.multiplicadorDeY
		dividendo = equationOne.multiplicadorDeX*equationTwo.multiplicadorDeY - equationOne.multiplicadorDeY*equationTwo.multiplicadorDeX
		if dividendo == 0:
			return None
		x = divisor/dividendo
		y = (equationOne.multiplicadorDeX*x + equationOne.sumando)/equationOne.multiplicadorDeY
		return x, y