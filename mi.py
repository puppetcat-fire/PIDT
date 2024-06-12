from jpype import *

implementingClass = "infodynamics.measures.continuous.kraskov.MutualInfoCalculatorMultiVariateKraskov1"

def mi(univariateSeries1, univariateSeries2):

	# univariateSeries1 = A[:,univariateSeries1Column]
	# univariateSeries2 = A[:,univariateSeries2Column]



	indexOfLastDot = implementingClass.rfind(".")
	implementingPackage = implementingClass[:indexOfLastDot]
	implementingBaseName = implementingClass[indexOfLastDot+1:]
	miCalcClass = eval('JPackage(\'%s\').%s' % (implementingPackage, implementingBaseName))
	print(miCalcClass)
	miCalc = miCalcClass()

	miCalc.initialise(1, 1)
	# b. Supply the observations to compute the PDFs from:
	miCalc.setObservations(JArray(JDouble, 1)(univariateSeries1), JArray(JDouble, 1)(univariateSeries2))
	# c. Make the MI calculation:
	miUnivariateValue = miCalc.computeAverageLocalOfObservations()
	return miUnivariateValue

