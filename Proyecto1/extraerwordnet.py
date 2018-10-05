
import lg.procesar as myOperation


rsp = myOperation.consultarDiccionarioMultilenguaje()
cont = 0
if (len(rsp) > 1):
    for item in rsp['data']:
        
        cont = cont + 1

        en = item['english']
        #separar por ;            
        lstSeparados = en.split('; ')
        for frase in lstSeparados:
            lngFrase = len(frase.split(None))
            if lngFrase == 1:
                if cont >= 3180:
                    #enviar palabra procesar con wordnet 
                    print('sending: ',frase, ' -> ',cont) 
                    myOperation.procesarConWordnet(frase)
                
                    


else:
    print('No se ha encontrado una respuesta')

