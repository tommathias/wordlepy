import ast

alphabet = {}
with open('answers.txt') as f:
  for line in f:
    word = line.split()[5]
    if len(word) != 5:
      print(f'word not found:{word}')
      continue
    for char in word:
      if char not in alphabet:
        alphabet[char] = 1
      else:
        alphabet[char] += 1
ranked = sorted(alphabet.items(), key=lambda l: l[1], reverse=True)
print(ranked)

#format data
data = ''
for k,v in ranked:
  data += f'{k} {v}\n'

with open('output\\rankedletters.txt', 'w') as f:
 f.write(data)