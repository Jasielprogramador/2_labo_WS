import urllib

import requests
import os;

from bs4 import BeautifulSoup

cookie = ""

def pdf_deskargatu(uria,izena):
    izena = str(izena).replace(' ', '_')
    metodoa = "GET"
    goiburuak = {'Host': 'egela.ehu.eus', 'Cookie': cookie}
    res = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
    pdf = res.content
    file = open("./pdfs/" + str(izena) + ".pdf", "wb")
    file.write(pdf)
    file.close()

def pdf_joan(content):
    soup = BeautifulSoup(content, 'html.parser')
    div_list = soup.find('div', {'class': 'resourceworkaround'})
    uria = div_list.find('a').get('href')
    list = uria.split('/')
    izena = list[len(list)-1]
    print(izena)
    pdf_deskargatu(uria,izena)

def irakasgaiko_pdf(uria):
    metodoa = "GET"
    goiburuak = {'Host': 'egela.ehu.eus', 'Cookie': cookie}
    erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
    html_kodea = erantzuna.content
    soup = BeautifulSoup(html_kodea, 'html.parser')

    div_list = soup.find_all('div', {'class': 'activityinstance'})
    for elem in div_list:
        if "pdf" in str(elem.find('img')['src']):
            izena = elem.find("span", {"class": "instancename"}).text
            uria = elem.find('a').get('href')
            erantzuna = requests.request(metodoa, uria, headers=goiburuak, allow_redirects=False)
            pdf_joan(erantzuna.content)

def sartuIrakasgaian(html):
    soup = BeautifulSoup(html, 'html.parser')
    a_links = soup.find_all("a", {'class': 'ehu-visible'})
    for elem in a_links:
        if elem.text == "Web Sistemak":
            u = elem.get('href')
            break
    irakasgaiko_pdf(u)

def sartuEgelan(erabiltzailea,pasahitza):
    global cookie
    metodo = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburuak = {'Host': 'egela.ehu.eus'}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    cookie = erantzuna.headers['Set-Cookie'].split(";")[0]
    host = "egela.ehu.eus"

    print("#######################################################")
    print("LEHENENGO ESKAERA")
    print("metodoa: "+metodo)
    print("uria: "+uria)
    print("cookie: " + cookie)
    print("edukia: " + edukia)
    print("host: " + host)

    if 'Location' in erantzuna.headers:
        uria = erantzuna.headers['Location']
    if 'Set-Cookie' in erantzuna.headers:
        cookie = erantzuna.headers['Set-Cookie'].split(",")[0]
    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("#######################################################")

    metodo = 'POST'
    uria = "https://"+host+"/login/index.php"
    goiburuak = {'Host':host,'Cookie':cookie,
                 'Content-Type':'application/x-www-form-urlencoded',
                 'Content-Length':'0'}
    edukia = {'username':erabiltzailea,'password':pasahitza}
    edukia_encoded = urllib.parse.urlencode(edukia)
    goiburuak['Content-Length'] = str(len(edukia_encoded))
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia_encoded, allow_redirects=False)

    if 'Location' in erantzuna.headers:
        uria = erantzuna.headers['Location']
    if 'Set-Cookie' in erantzuna.headers:
        cookie = erantzuna.headers['Set-Cookie'].split(",")[0]


    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia_encoded)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("#######################################################")

    metodo = 'GET'
    goiburuak = {'Host':host, 'Cookie':cookie}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    print("HIRUGARREN ESKAERA")
    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)

    print("#######################################################")

    metodo = 'GET'
    uria = "https://egela.ehu.eus/"
    goiburuak = {'Host': host, 'Cookie':cookie}
    edukia = ''
    erantzuna = requests.request(metodo, uria, headers=goiburuak, data=edukia, allow_redirects=False)

    print("LAUGARREN ESKAERA")

    print("metodoa: " + metodo)
    print("uria: " + uria)
    print("edukia: " + edukia)

    codigo = erantzuna.status_code
    descripcion = erantzuna.reason
    print(str(codigo) + " " + descripcion)
    sartuIrakasgaian(erantzuna.content)



if __name__ == '__main__':

    try:
        os.mkdir('pdfs')
    except OSError as e:
        print("Jada karpeta sortuta dago")

    username = input("Sar ezazu zure erabiltzailea\n")
    password = input("Sart ezazu zure pasahitza\n")
    sartuEgelan(username,password)
