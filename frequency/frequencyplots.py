import matplotlib.pyplot as pyplot
import ast

verbose = False
with open("output\\answersFrequency.txt") as f:
  answersStr = f.read()
answers = ast.literal_eval(answersStr)

answersLabels = []
answersData = []
for k,v in answers:
  answersLabels.append(k.upper())
  answersData.append(v)


with open("output\\validFrequency.txt") as f:
  validStr = f.read()
valid = ast.literal_eval(validStr)

validLabels = []
validData = []
for k,v in valid:
  validLabels.append(k.upper())
  validData.append(v)

fig, (answersAx, validAx) = pyplot.subplots(1, 2)
fig.suptitle('Valid Vs Answers Wordle Letter Frequency')

barWidth = 0.35

answersAx.barh(answersLabels, answersData, barWidth)
answersAx.set_xlabel('Frequency')
answersAx.set_ylabel('Letter')
answersAx.invert_yaxis()  # labels read top-to-bottom
answersAx.set_title('Wordle Answers Letter Frequency')


validAx.barh(validLabels, validData, barWidth)
validAx.set_xlabel('Frequency')
validAx.set_ylabel('Letter')
validAx.invert_yaxis()  # labels read top-to-bottom
validAx.set_title('Wordle Valid Letter Frequency')

pyplot.show()
fig.savefig('output\\answersVsValid.png')