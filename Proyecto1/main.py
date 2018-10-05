
import lg.procesar as myOperation


wrd = input('Ingresa una palabra kichwa: ')

rsp = myOperation.consultarKichwa(wrd)

if (len(rsp) > 1):
    es = rsp['data']['espanish']
    en = rsp['data']['english']
    sp = rsp['data']['speech']
    ca = rsp['data']['category']

    print(es,' - ',en,' - ',sp,' - ',ca)
        
    myOperation.workingWordNet(en) 

else:
    print('No se ha encontrado una respuesta')

