def main():
  aPosition = { "0": {}, "1": {}, "3": {}, "4": {}}
  wordCount = 0

  with open('answers.txt') as f:
    for line in f:
      word = line.split('\n')[0].split()[5]
      if len(word) != 5:
        print(f'word not found:{word}')
        continue
      wordCount += 1
      for i in [0,1,3,4]:
        stri = str(i)
        if word[i] == "A":
          if word[4] not in aPosition[stri]:
            aPosition[stri][word[4]] = 1
          else:
            aPosition[stri][word[4]] += 1

  for i in [0,1,3,4]:
    print("when A is in position " + str(i+1) + ", the final letter is:")
    ranked = sorted(aPosition[str(i)].items(), key=lambda l: l[1], reverse=True)
    print(ranked)

  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  totals = {}
  middleACount = 0

  for a in alphabet:
    for i in [0,1,3,4]:
      if a in aPosition[str(i)]:
        if a not in totals:
          totals[a] = aPosition[str(i)][a]
        else:
          totals[a] += aPosition[str(i)][a]
        middleACount += aPosition[str(i)][a]

  print('totals: ')
  ranked = sorted(totals.items(), key=lambda l: l[1], reverse=True)
  print(ranked)
  print()
  print("total words: " + str(wordCount))
  print("words with an middle yellow A: " + str(middleACount))
  print("yellow middle A, ending y: " + str(totals['Y']))
  print("percentage I guess, it's always hard: " + str((totals["Y"]/middleACount)*100)+"%")
  output = aPosition
  output["totals"] = totals
  with open("output\\ranked.txt", "w") as f:
    f.write(str(output))

main()