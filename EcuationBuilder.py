import Ecuation
import Line

def getMultiplierOfXIn(linea):
	return linea.pointB.y - linea.pointA.y

def getMultiplierOfYIn(linea):
	return linea.pointB.x - linea.pointA.x

def getSumando(linea):
	return (getMultiplierOfXIn(linea) * linea.pointA.x * -1) + (getMultiplierOfYIn(linea) * linea.pointA.y)

def getEquiationOfLine(line):
	return Ecuation.Ecuation(getMultiplierOfXIn(line), getMultiplierOfYIn(line), getSumando(line))