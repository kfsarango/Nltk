import json
import lg.processTranslate as myTranslate
import datetime
import time

cont  = 0
contNrTranslte  = 0
limitToSave = 0
lastContextTranslate = ''
lastContext = ''
newData = {}
newData['data'] = []



def buildJson(jsonMaster, idR, col, t):
    jsonMaster['data'].append({
                    'id': idR,
                    'col': col,
                    'translate': t
                })

def savingData(jsonMaster, fileName, cont):
    #saving file with traductions
    with open('src/'+ fileName +'.txt', 'w') as outfile:  
                json.dump(jsonMaster, outfile)
        
    #saving file with id
    savingLastId(cont)

def getLastId():
    try:
        f = open('src/lastid.txt', 'r')
        toLoad = f.readline()
        idFound = int(toLoad)
        f.close()
        print('Id encontrado: ', idFound)
        return idFound

    except Exception:
        print('Error al abrir el archivo lastid.txt')

def savingLastId(contador):
    f = open('src/lastid.txt', 'w')

    toSave = str(contador)

    f.write(toSave)

    print('Guardando ultimo id: ', contador)

    f.close()

#leyendo el json
with open('src/dataWorNet.txt') as json_file:  
    #load json
    data = json.load(json_file)

    #made name file to save
    now = datetime.datetime.now()
    nameFile = 'translate ' +  str(now)
    
    #load file with last id
    idtoStart = getLastId()
    limitToSave = idtoStart + 2000

    #Capturando errores
    try:
        #Recorriendo el json
        for p in data['data']:

            if cont >= idtoStart:
                idD = p['id']
                subject = p['subject']
                predicate = p['predicate']
                objectD = p['object']
                            
                if predicate == 'contexto':
                    if lastContext !=  subject:
                        #vamos a traducir con Google Translate
                        rspTranslate = myTranslate.translate_text('es',subject)
                        lastContextTranslate = rspTranslate
                        lastContext = subject
                        buildJson(newData, idD, 's',rspTranslate)
                        contNrTranslte = contNrTranslte + 1
                    else:
                        #armar el json con lastContextTranslate
                        buildJson(newData, idD, 's',lastContextTranslate)
                else:
                    
                    if (predicate != 'hipo') and (predicate != 'hipe'):
                        if predicate == 'sin':
                            if objectD == lastContext:
                                #armar el json con lastContextTranslate
                                buildJson(newData, idD, 'o',lastContextTranslate)
                            else:
                                #vamos a traducir con Google Translate
                                rspTranslate = myTranslate.translate_text('es',objectD)
                                buildJson(newData, idD, 'o',rspTranslate)
                                contNrTranslte = contNrTranslte + 1
                        else:
                            #vamos a traducir con Google Translate
                            rspTranslate = myTranslate.translate_text('es',objectD)
                            buildJson(newData, idD, 'o',rspTranslate)
                            contNrTranslte = contNrTranslte + 1
                        
                            
                
                if limitToSave == cont:
                    limitToSave = limitToSave  + 2000
                    savingData(newData, nameFile, cont)
                    print('aumentando contador y sleep(200s)')
                    print('GUARDANDO DATA en Contador: ',cont,' y IdData: ', idD)
                    time.sleep(200)


                print('\t\t>> row data nro: ', cont)
                print('Nro traducidos: ', contNrTranslte)
            
            
            cont = cont + 1

    except (Exception, KeyboardInterrupt):
          savingData(newData, nameFile, cont)
          print('\nOps! Something is wrong or has been interrupted\nSaving Data\nSALIENDO...')

