import json

with open('bayes.json') as bayes:
  by = json.load(bayes)
  print(by.keys())
  #print(by["wordFrequencyCount"])
  dc = by["docCount"]
  total = 0
  for key in dc.keys():
    if key == "misc":
      dc[key] = 105
    else:
      dc[key] = 100
    total += dc[key]
  wc = by["wordCount"]
  #for word in wc.keys():
  #  wc[word] = 100
  by["totalDocuments"] = total

with open('bayes.json','w') as bayes:
  json.dump(by, bayes)
