import urllib

import requests


def lehenegoEskaera():
    metodo = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburuak = {'Host': 'egela.ehu.eus'}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    cookie = erantzuna.headers['Set-Cookie'].split(";")[0]
    host = erantzuna.url.split("/")[2]

    print("metodoa:"+metodo)
    print("uria"+uria)
    print("cookie: " + cookie)
    print("host: " + host)


    #Esto para decir que tipo de respuesta hay
    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    return cookie,host


def bigarrenEskaera(cookie,host):
    metodo = 'POST'
    uria = "https://"+host
    cookieIzenburua = cookie.split("=")[0]
    cookieKodea = cookie.split("=")[1]
    goiburuak = {'Host':"'"+host+"'","'"+cookieIzenburua+"'":"'"+cookieKodea+"'",
                 'Content-Type':' application/x-www-form-urlencoded',
                 'Content-Length':'0'}
    edukia = '/login/index.php'
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

    print("metodoa:" + metodo)
    print("uria" + uria)
    print("edukia" + edukia)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

def hirugarrenEskaera():
    metodo = 'GET'
    uria = "https://" + host
    cookieIzenburua = cookie.split("=")[0]
    cookieKodea = cookie.split("=")[1]
    goiburuak = {'Host': "'" + host + "'", "'" + cookieIzenburua + "'": "'" + cookieKodea + "'"}
    edukia = '/login/index.php'
    print("Sartu e")
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    print("metodoa:" + metodo)
    print("uria" + uria)
    print("edukia" + edukia)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)



if __name__ == '__main__':

    cookie,host = lehenegoEskaera()
    bigarrenEskaera(cookie,host)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/