from jpype import *


def te(row1, row2):
    twoDTimeSeriesPython = []
    twoDTimeSeriesPython.append(row1)
    twoDTimeSeriesPython.append(row2)
    twoDTimeSeriesJavaInt = JArray(JInt, 2)(twoDTimeSeriesPython)

    teCalcClass = JPackage("infodynamics.measures.discrete").TransferEntropyCalculatorDiscrete
    teCalc = teCalcClass(2,1)
    teCalc.initialise()
    # Add observations of transfer across one cell to the right per time step:
    teCalc.addObservations(twoDTimeSeriesJavaInt, 1)
    result2D = teCalc.computeAverageLocalOfObservations()
    return result2D