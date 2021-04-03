import urllib

import requests
import sys


def lehenegoEskaera():
    metodo = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburuak = {'Host': 'egela.ehu.eus'}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    cookie = erantzuna.headers['Set-Cookie'].split(";")[0]
    host = erantzuna.url.split("/")[2]

    print("#######################################################")
    print("LEHENENGO ESKAERA")
    print("metodoa: "+metodo)
    print("uria: "+uria)
    print("cookie: " + cookie)
    print("edukia: " + edukia)
    print("host: " + host)



    #Esto para decir que tipo de respuesta hay
    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("#######################################################")

    return cookie,host


def bigarrenEskaera(cookie,host,erabiltzailea,pasahitza):
    metodo = 'POST'
    uria = "https://"+host+"/login/index.php"
    cookieIzenburua = cookie.split("=")[0]
    cookieKodea = cookie.split("=")[1]
    goiburuak = {'Host':host,cookieIzenburua:cookieKodea,
                 'Content-Type':'application/x-www-form-urlencoded',
                 'Content-Length':'0'}
    edukia = {'username':erabiltzailea,'password':pasahitza}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

    print("#######################################################")
    print("-------------------------------------------------------")
    print("BIGARREN ESKAERAREN LEHENGO HTTP ESKAERA (POST)")
    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia_encoded)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("-------------------------------------------------------")


    print("BIGARREN ESKAERAREN BIGARREN HTTP ESKAERA (GET)")
    metodo = 'GET'
    uria = erantzuna.headers['Location']
    goiburuak = {'Host': host, cookieIzenburua: cookieKodea}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("-------------------------------------------------------")

    print("#######################################################")

    return cookieIzenburua,cookieKodea,42336



def hirugarrenEskaera(cookieIzenburua,cookieKodea,id):
    metodo = 'GET'
    uria = "https://"+host+"/course/view.php"
    goiburuak = {'Host':host, cookieIzenburua:cookieKodea}
    edukia = {'id':id}
    edukia_encoded = urllib.parse.urlencode(edukia)
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

    print("HIRUGARREN ESKAERA")
    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia_encoded)



    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("#######################################################")

if __name__ == '__main__':
    cookie,host = lehenegoEskaera()

    print("Mesedez sartu ezazu zure erabiltzailea eta pasahitza","911806","Ani0045")
    cookieIzenburua,cookieKodea,id = bigarrenEskaera(cookie,host,"911806","Ani0045")
    hirugarrenEskaera(cookieIzenburua,cookieKodea,id)


    # print("Mesedez sartu ezazu zure erabiltzailea eta pasahitza",sys.argv[0],sys.argv[1])
    # bigarrenEskaera(cookie,host,sys.argv[0],sys.argv[1])
