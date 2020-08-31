
import numpy as np
import math as m

Y = list(np.arange(0.01,0.601,0.001))


def function(y):
	return 0.5805*m.log(y) + 5.9238
	
	

with open('./Geschwindigkeitsprofil.csv','w') as output:
	for y in Y:
		output.write(str(y) + ';' + str(function(y)) + '\n')