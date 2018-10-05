
import lg.procesar as myOperation


rsp = myOperation.consultarDiccionarioMultilenguaje()
cont = 0
cont2 = 0
if (len(rsp) > 1):
    for item in rsp['data']:
        
        en = item['english']
        #separar por ;
        lstSeparados = en.split('; ')

        for frase in lstSeparados:
            lngFrase = len(frase.split(None))
            if lngFrase > 1:
                cont = cont + 1
            else:
                print(frase)                
                cont2 = cont2 + 1

        
    print(cont, ' con mas de 2 palabras y ',cont2,' solo 1 palabra')    
    #myOperation.workingWordNet(en) 

else:
    print('No se ha encontrado una respuesta')

