import matplotlib.pyplot as pyplot
import ast

verbose = False
with open("output\\answersFrequency.txt") as f:
  dataStr = f.read()

ranked = ast.literal_eval(dataStr)

labels = []
data = []
for k,v in ranked:
  labels.append(k)
  data.append(v)

fig, ax = pyplot.subplots()

barWidth = 0.35

ax.barh(labels, data, barWidth)
ax.set_xlabel('Frequency')
ax.set_ylabel('Letter')
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_title('Wordle Answers list Letter Frequency')

#pyplot.show()
fig.savefig('output\\answersFrequency.png')