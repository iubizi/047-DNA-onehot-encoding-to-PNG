####################
# read file
####################

f = open('dna_output.txt', 'r')
lines = f.readlines()
f.close()

data = []

for line in lines:
    line = line.replace('\n', '') \
               .replace('a', '0') \
               .replace('c', '1') \
               .replace('g', '2') \
               .replace('t', '3')
    data.append( [ int(i) for i in line ] )

print( 'len(data) =', len(data) )
print()

####################
# onehot
####################

from tensorflow.keras.utils import to_categorical
import cv2
import numpy as np

for i in range(len(data)):
    onehot = to_categorical( data[i] )
    # print(onehot.shape)

    cv2.imwrite( 'pic/'+str(i)+'.png', np.transpose(onehot*255) )
    if i%100 == 0: print(i, end=' ')








