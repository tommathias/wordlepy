import re
import sys

#read args
guess = sys.argv[1].upper()
clues = sys.argv[2].lower()
excluded = ''
if len(sys.argv) > 3:
  excluded = sys.argv[3].upper()
verbose = False
debugging = False

#import answers
answers = []
with open('answers.txt') as f:
  for line in f:
    word = line.split()[5]
    if len(word) == 5: answers.append(word) #ignore invalid words
if verbose and debugging: print(answers)
#input current guess
if guess is None:
  guess = input('What is your guess?> ').upper()
if clues is None:
  clues = input('What clues did you get for this word (b=black, y=yellow, g=green)?> ').lower()

#validate info
if(re.match('^[A-Z]{5}$', guess) is None):
  sys.exit('five letters words only doofus')
if(re.match('^[byg]{5}$', clues) is None):
  sys.exit('Smooth move ex-lax - format the clues properly next time')

#match green by regex
regexString = '^'
greensCount = 0
yellowLetters = []

includedLetters = '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]'

for letter in excluded:
  includedLetters = includedLetters.replace(letter, '')

for i in range(0,5):
  if clues[i].lower() == 'g':
    regexString += guess[i]
    greensCount += 1
  else:
    if(clues[i].lower() == 'y'):
      yellowLetters.append(guess[i])
      regexString += includedLetters.replace(guess[i].upper(), '')
    else:
      regexString += includedLetters

regexString += '$'
if verbose: print(f'regex string: {regexString}')
regex = re.compile(regexString)

#could avoid running loop if no greens
if (greensCount == 0):
  sys.exit('hohoho green giant - include a green')

#process potential answers
result = []
for word in answers:
  if regex.match(word) is not None:
    if len(yellowLetters) == 0:
      result.append(word)
      continue
    for letter in yellowLetters:
      if(letter in word):
        result.append(word)
        break #avoid duplicates if multiple yellows match

#todo rank

#output potential answers
print(f'Narrowed it down to: {len(result)} word(s): {result}')