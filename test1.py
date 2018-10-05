from nltk.corpus import wordnet as wn

w1 = wn.synset('cat.n.01')
w2 = wn.synset('cat.n.01')

#print('Evaluando Similaridad: ', w1.wup_similarity(w2))

#lemmas
syn = wn.synsets('cookbooks')[0]
lemmas = syn.lemmas()
for item in lemmas:
    print(item.name())