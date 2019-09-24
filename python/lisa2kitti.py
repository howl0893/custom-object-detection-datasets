"""lisa2kitti.py: Converts LISA annotation files to
                  Kitti format bounding box label files
__author__ = "Matt Howlett"
"""

import os
import numpy as np

datasetDir = 'C:/Users/Matt/OneDrive/Documents/Kettering/courses/summer-2019/ce-senior-design/creating-kitti-datasets/cocosynth-master/datasets/LISA-annotations/daySequence1/'#

filename_in = 'frameAnnotationsBOX'
filename_out = 'traffic-sign-box-labels'

annFile = datasetDir + filename_in + '.txt'
labelFile = datasetDir + filename_out + '.txt'

catNms = ['stop', 'go', 'warning']

data = np.genfromtxt(annFile, dtype = 'unicode', delimiter = ';', usecols = (0,1,2,3,4,5,7))

img_filename = data[:,0]
category = data[:,1]
bbox1 = data[:,2]
bbox2 = data[:,3]
bbox3 = data[:,4]
bbox4 = data[:,5]
annID = data[:,6]

for i in range(len(img_filename)-1):
    with open(datasetDir + 'labels/' + '0000' + str(i) + '.txt', 'w') as label_file:
        out_str = str(category[i]) + ' 0 0 0 ' + str(bbox1[i]) + ' ' + str(bbox2[i]) + ' ' + str(bbox3[i])  + ' ' + str(bbox4[i]) + ' 0 0 0 0 0 0 0'
        label_file.write(out_str)