import re
answers = {'caxxy': [], 'cccay': [], 'otherA': [], 'noA': 0}
cAxxY = re.compile('^[a-z]a([a-z])\\1y')
cccAY = re.compile('^[a-z]{3}ay')

with open('answers.txt') as f:
  for line in f:
    word = line.split('\n')[0].split()[5].lower()
    #exclude words that aren't 5 letters
    if len(word) != 5:
      print(f'word not found:{word}')
      continue
    #match each form
    if cAxxY.match(word) is not None:
      answers['caxxy'].append(word)
      continue
    if cccAY.match(word) is not None:
      answers['cccay'].append(word)
      continue
    if word[0] == 'a' or word[4] == 'a':
      answers['otherA'].append(word)
      continue
    answers['noA'] += 1
print(answers)
