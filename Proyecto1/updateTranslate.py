import json
import dt.servicerest as myService

#leyendo el json
with open('../Respaldos/translateV4.txt') as json_file:  
    data = json.load(json_file)
    
    for p in data['data']:
        idData = p['id']
        translate = p['translate']
        print('Sending: id-> ', idData, ' | transalate-> ', translate)
        myService.updateTranslate(idData, translate)

        

