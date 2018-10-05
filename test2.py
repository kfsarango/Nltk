from nltk.corpus import wordnet as wn

synonyms = []
antonyms = []

word = input("Ingresa una palabra: ")

#for syn in wn.synsets(word):
    #print(syn.hyponyms())

print('-----------------')

for syn in wn.synsets(word):
    context = syn.name()
    definition = syn.definition()
    examples = syn.examples()

    print('Contexto: ', context)
    print('Definition: ', definition)
    print('Examples: ')
    for x in examples:
        print(x)
    print('Lemas:')
    for l in syn.lemmas():
        #sinonimos
        synonyms = l.name()
        print('\t',synonyms)
        if l.antonyms():
            antonyms = l.antonyms()[0].name()
            print('\tANT -> ', antonyms)
    
    hyponyms = syn.hyponyms()
    print('Hipónimos:')
    for hy in hyponyms:
        print('\t',hy.name())

    hypernyms = syn.hypernyms()
    print('Hiperónimos:')
    for hy in hypernyms:
        print('\t',hy.name())
    