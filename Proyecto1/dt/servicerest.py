import requests
import json


def queryItemMultilenguaje(text):
    res = requests.get('http://127.0.0.1:4567/multilenguaje/'+text)

    if res.status_code != 200:
        # algo salio mal
        raise ApiError('GET /multilenguaje/ {}'.format(resp.status_code))


    data_string = json.dumps(res.json())


    return json.loads(data_string)

def queryAllWordnet():
    res = requests.get('http://127.0.0.1:4567/wordnet')

    if res.status_code != 200:
        # algo salio mal
        raise ApiError('GET /wordnet/ {}'.format(resp.status_code))


    data_string = json.dumps(res.json())


    return json.loads(data_string)

def queryAllMultilenguaje():
    res = requests.get('http://127.0.0.1:4567/multilenguaje')

    if res.status_code != 200:
        # algo salio mal
        raise ApiError('GET /multilenguaje/ {}'.format(resp.status_code))


    data_string = json.dumps(res.json())


    return json.loads(data_string)

def queryComprobarRecurso(text):
    res = requests.get('http://127.0.0.1:4567/comprobar/'+text)

    if res.status_code != 200:
        # algo salio mal
        raise ApiError('GET /comprobar/ {}'.format(resp.status_code))


    data_string = json.dumps(res.json())


    return json.loads(data_string)

def insertData(sub, pre, obj):
    data = {
        "id": 0, 
        "subject": sub, 
        "predicate": pre,
        "object": obj
    }

    data_json = json.dumps(data)

    headers = {'Content-type': 'application/json'}

    response = requests.post('http://127.0.0.1:4567/recurso', data=data_json, headers=headers)

    return response

def updateTranslate(idD, translate):
    data = {
        "id": idD, 
        "subject": '', 
        "predicate": '',
        "object": '',
        "translate": translate
    }

    data_json = json.dumps(data)

    headers = {'Content-type': 'application/json'}

    response = requests.post('http://127.0.0.1:4567/addtranslate', data=data_json, headers=headers)

    return response