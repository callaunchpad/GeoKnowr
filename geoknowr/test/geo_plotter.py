import numpy as np
import sys
import pdb

from PIL import Image
from numpy import genfromtxt
from matplotlib import pyplot as plt
from matplotlib.pyplot import draw
from matplotlib import figure as fig
import xml.etree.ElementTree as ET
import matplotlib
import matplotlib.path as mplPath

import re

sys.path.append('../sampler')  
import location_sampler

states_file = '../sampler/states.xml'

borders= location_sampler.get_borders(states_file)
labels= location_sampler.get_labels(states_file)

#location_sampler.plot_map(borders)
nLabels = len(borders)

# generate border map of USA
for i in range(0,nLabels):
    plt.plot(borders[i][:,0], borders[i][:,1], 'r-')
plt.show(0)
plt.hold(True)

for states in range(1,3):
	print labels[states]
	fname = "../images/" + labels[states] + "/info.txt"

	with open(fname) as f:
	    content = f.readlines()
	f.close()
	content = [x.strip() for x in content] 

	points = np.zeros((len(content), 2))

	for j in range(0,len(content)):
		matches = re.finditer(" [+-]?([0-9]*[.])?[0-9]+", content[j])

		count = 0
		pos = [0,0]
		for matchNum, match in enumerate(matches):
			matchNum = matchNum + 1
			pos[count] = float(match.group())
			count +=1

		points[j][0] = pos[0]
		points[j][1] = pos[1]

		#print content[0]
	# plot lat,lng on map
	plt.plot(points[:,1], points[:,0], 'b.', markersize=2)
	plt.pause(0.05)

pdb.set_trace()
