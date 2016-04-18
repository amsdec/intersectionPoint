import PointInputParser
import Point
import Line
import IntersectionPointFinder

def getLine(line):
    return Line.Line(getPont("A", line), getPont("B", line))

def getPont(point, line):
	return PointInputParser.parseText(str(raw_input("Punto " + str(point) + " de la linea" + str(line) + " (en formato x,y): ")))

print IntersectionPointFinder.find(getLine(1), getLine(2))
