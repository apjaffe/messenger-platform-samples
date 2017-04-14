from nltk.corpus import wordnet as wn

def expand_synset(cat):
  food = wn.synset(cat)
  foods = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
  foods2 = [f.replace("_"," ") for f in foods]
  return "\n".join(foods2)

#open("rawcats/food2","w").write(expand_synset('food.n.02'))
#open("rawcats/food3","w").write(expand_synset('restaurant.n.01'))
#open("rawcats/food4","w").write(expand_synset('grocery_store.n.01'))
#open("rawcats/food5","w").write(expand_synset('market.n.05'))
#open("rawcats/food6","w").write(expand_synset('food.n.01'))
#open("rawcats/food7","w").write(expand_synset('eat.v.02'))
#open("rawcats/entertainment2","w").write(expand_synset('leisure.n.01'))
#open("rawcats/entertainment3","w").write(expand_synset('outing.n.01'))
#open("rawcats/entertainment4","w").write(expand_synset('entertainment.n.01'))
#open("rawcats/entertainment5","w").write(expand_synset('movie.n.01'))
#open("rawcats/entertainment6","w").write(expand_synset('play.n.01'))
#open("rawcats/education2","w").write(expand_synset('school.n.01'))
#open("rawcats/education3","w").write(expand_synset('book.n.01'))
#open("rawcats/housing2","w").write(expand_synset('house.n.01'))
#open("rawcats/housing3","w").write(expand_synset('apartment.n.01'))
#open("rawcats/housing4","w").write(expand_synset('housing.n.01'))
#open("rawcats/housing5","w").write(expand_synset('live.v.01'))


open("rawcats/misc2","w").write(expand_synset('spend.v.01'))
