import json
import time

cont  = 0
contNrTranslte  = 0
limitToSave = 15877
lastContextTranslate = ''
lastContext = ''
newData = {}
newData['data'] = []

#leyendo el json
with open('../Respaldos/translateV8.txt') as json_file:  
    data = json.load(json_file)
    print('First')
    print(data['data'][0]['id'])
    print(data['data'][0]['col'])
    print(data['data'][0]['translate'])

    lng = len(data['data'])
    print('\nLast: ', lng)
    lng = lng - 1
    print(data['data'][lng]['id'])
    print(data['data'][lng]['col'])
    print(data['data'][lng]['translate'])

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

    '''
    for p in data['data']:
        print(p['id'])
        print(p['col'])
        print(p['translate'])
        print('\t\t>> row data nro: ', cont)
        
        
        cont = cont + 1'''
        

