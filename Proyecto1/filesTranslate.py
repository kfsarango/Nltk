import json
import time


#leyendo el json

nroFile = 1

while nroFile < 35: #charlie empieza desde 25-28 // last file large: 160379 id
    nameFile = 'translateV' + str(nroFile)
    nroFile = nroFile + 1
    fileToOpen = '../Respaldos/'+nameFile+'.txt'
    with open(fileToOpen) as json_file:  
        data = json.load(json_file)
        print('->\t',nameFile, '\nFirst')
        print(data['data'][0]['id'])
        print(data['data'][0]['col'])
        print(data['data'][0]['translate'])

        lng = len(data['data'])
        print('\nLast: ')
        lng = lng - 1
        print(data['data'][lng]['id'])
        print(data['data'][lng]['col'])
        print(data['data'][lng]['translate'])
        print('\n\n\n')

    '''
                              id        translate
        ------------------------------------------
        TranslateV1 File:   1     ->    esperanza
                            2127  ->    un experto en cocina cuyo libro de cocina ha sido sometido a muchas ediciones (1857-1915)
        ------------------------------------------
        TranslateV2 File:   2127  ->    un experto en cocina cuyo libro de cocina ha sido sometido a muchas ediciones (1857-1915)
                            3877  ->    Escritor francés conocido por sus obras sobre los derechos de las mujeres y la independencia (1804-1876)
        ------------------------------------------
        TranslateV3 File:   3878  ->    Arena
                            14878 ->    limitado o por debajo del promedio en número o cantidad o magnitud o extensión
        ------------------------------------------
        TranslateV4 File:   14878 ->    limitado o por debajo del promedio en número o cantidad o magnitud o extensión
                            20878 ->    el frio comun
        ------------------------------------------
        TranslateV5 File:   20876 ->    el hombre comun
                            25876 ->    doblar para parecerse una cruz
        ------------------------------------------
        TranslateV6 File:   72876 ->    seno
                            85874 ->    doblar para parecerse una cruz
        ------------------------------------------
        TranslateV7 File:   25877 ->    ella cruzo sus piernas
                            30877 ->    sostenga el cepillo para
        ------------------------------------------
        TranslateV8 File:   30875 ->    asi
                            32875 ->    Continuó teniendo fuertes dolores de cabeza y en consecuencia regresó al médico.
    
    '''

        

