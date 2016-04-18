import Point

def parseText(input):
	x = int(input[:input.index(",")])
	y = int(input[input.index(",") + 1 :])
	return Point.Point(x, y)
		