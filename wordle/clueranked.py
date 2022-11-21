import re, sys
from xml.etree.ElementInclude import include

# example calls:
# raise bbybg ras / biome bgbyg rasbo / mince ggggg
# rates bbbgb rats / novel bbbgb ratsnovl / cheek ggggg
# plane yyybg n / maple yyggg n / ample ggggg
# licks yybbb cks / elite bgybb cksete / plain bgggb cksetepn / flair ggggg
# goose yybbb ose / organ yyyyb osen / cargo ggggg

#read args
#todo flags vs args
#todo change to valid list, not answers list
#todo build as library and create cli and looped input
guess = ''
clues = ''
excludedLetters = ''
if len(sys.argv) > 1:
  guess = sys.argv[1].upper()
if len(sys.argv) > 2:
  clues = sys.argv[2].lower()
if len(sys.argv) > 3:
  excludedLetters = sys.argv[3].upper()

#set execution flags
#todo use -v flag
verbose = False
debugging = False

def loadAnswers():
  answers = []
  with open('answers.txt') as f:
    for line in f:
      word = line.split()[5]
      if len(word) == 5: answers.append(word) #ignore invalid words
  if verbose and debugging: print(answers)
  return answers

def loadScores():
  scores = {}
  with open("letterranks.txt") as f:
    for line in f:
      split = line.split()
      scores[split[0]] = split[1]
  if verbose and debugging: print(scores)
  return scores

def getGuess():
  global guess
  if guess == '':
    guess = input('What is your guess?> ').upper()
  if(re.match('^[A-Z]{5}$', guess) is None):
    sys.exit('five letters words only doofus')

def getClues():
  global clues
  if clues == '':
    clues = input('What clues did you get for this word (b=black, y=yellow, g=green)?> ').lower()
  if(re.match('^[byg]{5}$', clues) is None):
    sys.exit('Smooth move ex-lax - format the clues properly next time')

def getArgs():
  global guess, clues, excludedLetters
  args = input ('Enter your guess, clues (g=green, y=yellow, b=black e.g. gbbyg) and excluded letters: ')
  splitArgs = args.split(' ')
  if debugging: print(splitArgs)
  guess = splitArgs[0].upper()
  clues = splitArgs[1].lower()
  if len(splitArgs) > 2:
    excludedLetters = splitArgs[2].upper()

  #todo validate args 
  if debugging:
    print(guess)
    print(clues)

def excludeLetters():
  #todo match e.g. goose yybbb where exactly one letter exists
  global excludedLetters, includedLetters
  for letter in excludedLetters:
    includedLetters = includedLetters.replace(letter, '')
  if verbose or debugging: print(f'letters after exclusion: {includedLetters}')

def buildRegex():
  global clues, yellowLetters, includedLetters
  regexString = '^'
  for i in range(5):
    if clues[i].lower() == 'g':
      regexString += guess[i]
    else:
      if(clues[i].lower() == 'y'):
        yellowLetters.append(guess[i])
        regexString += includedLetters.replace(guess[i].upper(), '')
      else:
        regexString += includedLetters

  regexString += '$'
  if verbose: print(f'regex string: {regexString}')
  regex = re.compile(regexString)

  if debugging: print(regex)
  return regex

def rankWord(word, clues) -> int:
  score = 0
  for i in range(5):
    if (clues[i].lower() == 'g'): continue #rank only based on unguessed letters
    score += int(scores[word.upper()[i]])
  return score

def matchesClues(word) -> bool:
  global regex, excludedLetters, yellowLetters
  bregex = regex.match(word) is not None
  bincluded = all(character in word for character in yellowLetters)
  bexcluded = not any(character in word for character in list(excludedLetters))
  isMatch = bregex and bincluded and bexcluded
  if debugging and isMatch: print(f'{word} match? {isMatch}')
  return isMatch

def findAnswers() -> dict:
  #process potential answers
  global answers, regex, yellowLetters
  result = {}
  for word in answers:
    if matchesClues(word):
      if len(yellowLetters) == 0:
        result[word] = rankWord(word, clues)
        continue
      for letter in yellowLetters:
        if(letter in word):
          result[word] = rankWord(word, clues)
          break #avoid duplicates if multiple yellows match
  return result

answers = loadAnswers()
scores = loadScores()

yellowLetters = []
includedLetters = '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]'

while clues != 'ggggg':
  getArgs()
  if clues == 'ggggg': continue

  excludeLetters()
  regex = buildRegex()

  result = findAnswers()
  rankedAnswers = sorted(result.items(), key=lambda l: l[1], reverse=True)

  #output potential answers
  print(f'Narrowed it down to: {len(rankedAnswers)} word(s): {rankedAnswers}')
print('Thank you for playing Wing Commander')