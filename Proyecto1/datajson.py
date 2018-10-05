import json
import lg.procesar as myOperation

rsp = myOperation.consultarDataWornet()

#para exportar toda la informacion desde wordnet
'''with open('src/dataWorNet.txt', 'w') as outfile:  
    json.dump(rsp, outfile)

print('exportando')'''

