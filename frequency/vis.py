import matplotlib.pyplot as plt
import ast
#import ayend

verbose = False
#ayend.main()

with open("output\\ranked.txt") as f:
  dataStr = f.read()

rawData = ast.literal_eval(dataStr)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
data = {}
labels = []
for a in alphabet:
  data[a] = 0
  labels.append(a)

position1 = []
position2 = []
position4 = []
position5 = []

#populate a dataset keyed to the alphabet from the ordered results
def populate(target, raw):
  for a in alphabet:
    if a in raw:
      target.append(raw[a])
    else:
      target.append(0)
  if verbose: print(target)

if verbose:
  print()
  print("from raw data")
  sumY = 0
  for i in [0,1,3,4]:
    if 'Y' in rawData[str(i)]:
      print(f"pos{i} Y: {rawData[str(i)]['Y']}")
      sumY += rawData[str(i)]['Y']
  print(f"totals Y: {rawData['totals']['Y']}")
  print(f"sum Y: {sumY}")

populate(position1, rawData['0'])
populate(position2, rawData['1'])
populate(position4, rawData['3'])
populate(position5, rawData['4'])


if verbose:
  print()
  print(f"pos1 Y: {position1[24]}")
  print(f"pos2 Y: {position2[24]}")
  print(f"pos4 Y: {position4[24]}")
  print(f"pos5 Y: {position5[24]}")
  print(f"sum Y: {position1[24] + position2[24] + position4[24] + position5[24]}")


def combine(bottom, arr):
  for i in range(0,25):
    bottom[i] += arr[i]

fig, ax = plt.subplots()

barWidth = 0.35
ax.bar(labels, position1, barWidth, label='Position 1')
bottom = position1[:] #make a copy using slice
ax.bar(labels, position2, barWidth, label='Position 2', bottom=bottom)
combine(bottom, position2)
ax.bar(labels, position4, barWidth, label='Position 4', bottom=bottom)
combine(bottom, position4)
ax.bar(labels, position5, barWidth, label='Position 5', bottom=bottom)

ax.set_xlabel('final letter')
ax.set_title('Final letter, by A position')
ax.legend()

fig.savefig('output\\stackedbars.png')
plt.show()