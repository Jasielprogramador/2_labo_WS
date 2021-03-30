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

    print("metodoa: "+metodo)
    print("uria: "+uria)
    print("cookie: " + cookie)
    print("host: " + host)


    #Esto para decir que tipo de respuesta hay
    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    return cookie,host


def bigarrenEskaera(cookie,host,erabiltzailea,pasahitza):
    metodo = 'POST'
    uria = "https://"+host+"/login/index.php"
    cookieIzenburua = cookie.split("=")[0]
    cookieKodea = cookie.split("=")[1]
    goiburuak = {'Host':"'"+host+"'","'"+cookieIzenburua+"'":"'"+cookieKodea+"'",
                 'Content-Type':'application/x-www-form-urlencoded',
                 'Content-Length':'0'}
    edukia = {'username':erabiltzailea,'password':pasahitza}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia_encoded)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print(erantzuna.content)

# def hirugarrenEskaera():
#     metodo = 'GET'
#     uria = "https://" + host
#     cookieIzenburua = cookie.split("=")[0]
#     cookieKodea = cookie.split("=")[1]
#     goiburuak = {'Host': "'" + host + "'", "'" + cookieIzenburua + "'": "'" + cookieKodea + "'"}
#     edukia = '/login/index.php'
#     print("Sartu e")
#     erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)
#
#     print("metodoa:" + metodo)
#     print("uria" + uria)
#     print("edukia" + edukia)
#
#     codigo = erantzuna.status_code
#     descripcion = erantzuna.reason
#     print(str(codigo) + " " + descripcion)



if __name__ == '__main__':
    cookie,host = lehenegoEskaera()

    print("Mesedez sartu ezazu zure erabiltzailea eta pasahitza","123333","12121212")
    bigarrenEskaera(cookie,host,"121212","1212121")


    # print("Mesedez sartu ezazu zure erabiltzailea eta pasahitza",sys.argv[0],sys.argv[1])
    # bigarrenEskaera(cookie,host,sys.argv[0],sys.argv[1])
