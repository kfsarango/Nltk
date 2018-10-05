from nltk.corpus import wordnet
import dt.servicerest as myRest

def consultarKichwa(word):
    return myRest.queryItemMultilenguaje(word)

def consultarDataWornet():
    return myRest.queryAllWordnet()


def workingWordNet(word):
    resp = myRest.queryComprobarRecurso(word)
    if len(resp) == 1:
        saveData(findSinonyms(word), word, 'sin')
        saveData(findAntonyms(word), word, 'ant')
        saveData(findHypernomys(word), word, 'hyp')
        saveData(findHyponomys(word), word, 'hypo')
        saveData(findDefinition(word), word, 'def')
        saveData(findExamples(word), word, 'ex')
    else:
        print('Esta palabra: ', word, ' Ya han sido guardados sus datos Wordnet')
    



def findSinonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms

def findAntonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():     
                antonyms.append(l.antonyms()[0].name())
    return antonyms

def findHypernomys(word):
    hipernyms = []
    hiper = wordnet.synset(word+'.n.01')
    for hyper in hiper.hypernyms():
        hipernyms.append(hyper.name())
    return hipernyms

def findHyponomys(word):
    hiponyms = []
    hipo = wordnet.synset(word+'.n.01')
    for hy in hipo.hyponyms():
        hiponyms.append(hy.name())
    return hiponyms

def findDefinition(word):
    definition = []
    rsp = wordnet.synset(word+'.n.01').definition()
    definition.append(rsp)
    return definition

def findExamples(word):
    examples = []
    rsp = wordnet.synset(word+'.n.01').examples()
    for item in rsp:
        examples.append(item)
    return examples

def saveData(lista, word, predicate):
    if len(lista) > 0:
        print('-> Guardando '+predicate)
        for x in lista:
            myRest.insertData(word,predicate,x)


#Para obtener y guardar datos obtenidos desde wordnet
def consultarDiccionarioMultilenguaje():
    return myRest.queryAllMultilenguaje()

def procesarConWordnet(word):
    resp = myRest.queryComprobarRecurso(word)
    if len(resp) == 1:
        #empezamos a buscar con wordnet        
        for syn in wordnet.synsets(word):
            context = syn.name()
            response = myRest.insertData(word,'contexto',context)
            #print('Insertando: | ',word,' - contexto - ',context,' | Con RSP = ',response)
            #contInserts = contInserts + 1

            definition = syn.definition()
            response = myRest.insertData(context,'definicion',definition)

            #obtenemos ejemplos para un contexto
            examples = syn.examples()
            for x in examples:
                response = myRest.insertData(context,'ejemplo',x)
                
            
            #obtenemos los lemas (sinónimos y antónimos)
            for l in syn.lemmas():
                #sinonimos
                synonyms = l.name()
                response = myRest.insertData(context,'sin',synonyms)
                

                #comprobamos si tiene un antónimo
                if l.antonyms():
                    antonyms = l.antonyms()[0].name()
                    response = myRest.insertData(context,'ant',antonyms)
                    
            
            hyponyms = syn.hyponyms()
            #buscamos 'Hipónimos'
            for hy in hyponyms:
                response = myRest.insertData(context,'hipo',hy.name())
                

            hypernyms = syn.hypernyms()
            #buscamos 'Hiperónimos:'
            for hy in hypernyms:
                response = myRest.insertData(context,'hipe',hy.name())
                
                        
    else:
        print('Esta palabra: | ', word, ' | Ya han sido guardados sus datos Wordnet') 
        
    


