import json
import dt.servicerest as myService

nroFile = 31

#leyendo el json

while nroFile < 35: #charlie empieza desde 25-28
    nameFile = 'translateV' + str(nroFile)
    nroFile = nroFile + 1
    fileToOpen = '../Respaldos/'+nameFile+'.txt'
    with open(fileToOpen) as json_file:

        data = json.load(json_file)
        print('->\t',nameFile, ' en proceso')
        for p in data['data']:
            idData = p['id']
            translate = p['translate']
            myService.updateTranslate(idData, translate)
            print(idData)

        #log de los archivos traducidos
        print('\nFirst')
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

        

