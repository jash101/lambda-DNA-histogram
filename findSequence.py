from matplotlib import pyplot as plt 
import numpy as np 

with open('DNAinput.txt', 'r') as file:
    dnaSequence = file.read().replace('\n', '')

searchSequence = "GG"

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

print(len(dnaSequence))
res = [translate(i, 0, len(dnaSequence), 0, 5.94) for i in range(len(dnaSequence)) if dnaSequence.startswith(searchSequence, i)]
print(str(res))   

resnp = np.asarray(res)
  
# Creating histogram 
fig, ax = plt.subplots(figsize =(10, 7)) 
nbins = 600
ax.hist(resnp, bins = nbins) 
# Show plot 
plt.show()

#TODO output txt file of occurrences
