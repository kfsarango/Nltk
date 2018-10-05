import nltk
import sqlite3
from nltk.corpus import wordnet
synonyms = []
antonyms = []
hipernyms = []
hiponyms = []

word = input("Ingresa una palabra: ")

for syn in wordnet.synsets(word):
    print(syn)
    #print(syn.name(), ' - ' , syn.lemma_names())
    for l in syn.lemmas():
        print(l.name(),' -> ',syn.definition())
        synonyms.append(l.name())

        if l.antonyms():     
            antonyms.append(l.antonyms()[0].name())


hipo = wordnet.synset(word+'.n.01')
for hy in hipo.hyponyms():
    hiponyms.append(hy.name())

hiper = wordnet.synset(word+'.n.01')
for hyper in hiper.hypernyms():
    hipernyms.append(hyper.name())

print('\nDEFINICION:')
print(wordnet.synset(word+'.n.01').definition())

print('\nEJEMPLOS:')
print(wordnet.synset(word+'.n.01').examples())

print('\t\tLista de sinonimos')
for sin in synonyms:
    print(sin)

print('\t\tLista de antonimos')
for ant in antonyms:
    print(ant)

print('\t\tLista hiperonimos')
for hip in hipernyms:
    print(hip)

print('\t\tLista hiponimos')
for hipo in hiponyms:
    print(hipo)