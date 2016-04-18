import EcuationBuilder
import Ecuation
import EquationResolver

def buidEquationFromLine(line):
	ecuation = EcuationBuilder.getEquiationOfLine(line)
	print ("La ecuacion que define a la linea " + line.toString() + " es " + ecuation.toString())
	return ecuation

def find(lineaUno, lineaDos):
	print("Se busca el punto de interseccion entre las lineas " + lineaUno.toString() + " y " + lineaDos.toString())
	ecuationLineOne = buidEquationFromLine(lineaUno)
	ecuationLineTwo = buidEquationFromLine(lineaDos)
	return EquationResolver.EquationResolver().findValue(ecuationLineOne, ecuationLineTwo)
	

